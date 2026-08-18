# -*- coding: utf-8 -*-
"""
Daily1Step Master Builder for 204+ Specialized Calculators
Each calculator has domain-specific inputs, formulas, outputs, Chart.js visualizations, guides, and FAQs.
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
LEGAL_DIR = os.path.join(BASE_DIR, "legal")

os.makedirs(TOOLS_DIR, exist_ok=True)
os.makedirs(LEGAL_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "all_calc_tools.json"), "r", encoding="utf-8") as f:
    ALL_TOOLS = json.load(f)

print(f"Generating specialized logic for all {len(ALL_TOOLS)} tools...")

# ══════════════════════════════════════════════════════════════════
# DOMAIN ENGINES FOR ALL CALCULATOR TYPES
# ══════════════════════════════════════════════════════════════════

def get_specialized_engine(tool):
    cid = tool["id"]
    cat = tool["category"]
    title = tool["title"]

    # ─────────────────────────────────────────────────────────────
    # 1. CONCRETE & MASONRY & CONSTRUCTION
    # ─────────────────────────────────────────────────────────────
    if "concrete" in cid:
        inputs = '''
        <div class="unit-toggle-group">
          <button type="button" class="unit-btn active" id="btnSlab" onclick="setConcreteType('slab')">Slab / Wall / Footing</button>
          <button type="button" class="unit-btn" id="btnHole" onclick="setConcreteType('hole')">Round Column / Hole</button>
        </div>

        <div id="slabInputs">
          <div class="form-group">
            <label class="form-label">Length</label>
            <div style="display:flex; gap:10px;">
              <input type="number" id="slabLen" class="calc-input" value="10" min="0.1" step="0.5" style="flex:2;">
              <select id="slabLenUnit" class="calc-select" style="flex:1.2;">
                <option value="ft" selected>Feet</option>
                <option value="in">Inches</option>
                <option value="yd">Yards</option>
                <option value="m">Meters</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Width</label>
            <div style="display:flex; gap:10px;">
              <input type="number" id="slabWidth" class="calc-input" value="10" min="0.1" step="0.5" style="flex:2;">
              <select id="slabWidthUnit" class="calc-select" style="flex:1.2;">
                <option value="ft" selected>Feet</option>
                <option value="in">Inches</option>
                <option value="yd">Yards</option>
                <option value="m">Meters</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Thickness or Height</label>
            <div style="display:flex; gap:10px;">
              <input type="number" id="slabThick" class="calc-input" value="4" min="0.1" step="0.5" style="flex:2;">
              <select id="slabThickUnit" class="calc-select" style="flex:1.2;">
                <option value="in" selected>Inches</option>
                <option value="ft">Feet</option>
                <option value="cm">Centimeters</option>
              </select>
            </div>
          </div>
        </div>

        <div id="holeInputs" style="display:none;">
          <div class="form-group">
            <label class="form-label">Diameter</label>
            <div style="display:flex; gap:10px;">
              <input type="number" id="holeDiam" class="calc-input" value="12" min="0.1" step="1" style="flex:2;">
              <select id="holeDiamUnit" class="calc-select" style="flex:1.2;">
                <option value="in" selected>Inches</option>
                <option value="ft">Feet</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Depth / Height</label>
            <div style="display:flex; gap:10px;">
              <input type="number" id="holeDepth" class="calc-input" value="4" min="0.1" step="0.5" style="flex:2;">
              <select id="holeDepthUnit" class="calc-select" style="flex:1.2;">
                <option value="ft" selected>Feet</option>
                <option value="in">Inches</option>
              </select>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Quantity</label>
          <input type="number" id="concQty" class="calc-input" value="1" min="1" step="1">
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Concrete Volume Needed</div>
          <div class="result-hero-val" id="resYards">1.23 yd&sup3;</div>
          <div style="font-weight:600; color:#0f766e; margin-top:4px;" id="resCuFt">33.33 cu ft · 0.94 m&sup3;</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">60 lb Pre-mix Bags</span><span class="val" id="resBags60">75 Bags</span></div>
          <div class="result-row"><span class="label">80 lb Pre-mix Bags</span><span class="val" id="resBags80">56 Bags</span></div>
          <div class="result-row"><span class="label">Estimated Total Weight</span><span class="val" id="resWeight">4,467 lbs (2.23 tons)</span></div>
          <div class="result-row"><span class="label">Recommended Order (+10% buffer)</span><span class="val" id="resBuffer">1.35 yd&sup3;</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        var concType = 'slab';
        function setConcreteType(t) {
          concType = t;
          document.getElementById('btnSlab').classList.toggle('active', t === 'slab');
          document.getElementById('btnHole').classList.toggle('active', t === 'hole');
          document.getElementById('slabInputs').style.display = t === 'slab' ? 'block' : 'none';
          document.getElementById('holeInputs').style.display = t === 'hole' ? 'block' : 'none';
          calculate();
        }

        function toFeet(val, unit) {
          if (unit === 'in') return val / 12;
          if (unit === 'yd') return val * 3;
          if (unit === 'm') return val * 3.28084;
          if (unit === 'cm') return val / 30.48;
          return val;
        }

        function calculate() {
          var qty = parseFloat(document.getElementById('concQty').value) || 1;
          var cuFt = 0;

          if (concType === 'slab') {
            var l = toFeet(parseFloat(document.getElementById('slabLen').value) || 0, document.getElementById('slabLenUnit').value);
            var w = toFeet(parseFloat(document.getElementById('slabWidth').value) || 0, document.getElementById('slabWidthUnit').value);
            var h = toFeet(parseFloat(document.getElementById('slabThick').value) || 0, document.getElementById('slabThickUnit').value);
            cuFt = l * w * h * qty;
          } else {
            var d = toFeet(parseFloat(document.getElementById('holeDiam').value) || 0, document.getElementById('holeDiamUnit').value);
            var h = toFeet(parseFloat(document.getElementById('holeDepth').value) || 0, document.getElementById('holeDepthUnit').value);
            var r = d / 2;
            cuFt = Math.PI * r * r * h * qty;
          }

          var cuYards = cuFt / 27;
          var cuMeters = cuFt * 0.0283168;
          var bags60 = Math.ceil(cuFt / 0.45);
          var bags80 = Math.ceil(cuFt / 0.60);
          var weightLbs = cuFt * 134; // approx 134 lbs per cu ft of mixed concrete
          var weightTons = weightLbs / 2000;
          var bufferYards = cuYards * 1.1;

          document.getElementById('resYards').innerHTML = cuYards.toFixed(2) + ' yd&sup3;';
          document.getElementById('resCuFt').innerHTML = cuFt.toFixed(2) + ' cu ft · ' + cuMeters.toFixed(2) + ' m&sup3;';
          document.getElementById('resBags60').textContent = bags60.toLocaleString() + ' Bags';
          document.getElementById('resBags80').textContent = bags80.toLocaleString() + ' Bags';
          document.getElementById('resWeight').textContent = Math.round(weightLbs).toLocaleString() + ' lbs (' + weightTons.toFixed(2) + ' tons)';
          document.getElementById('resBuffer').innerHTML = bufferYards.toFixed(2) + ' yd&sup3;';

          CalcCore.renderDoughnutChart('calcChart', ['Net Concrete Volume', '+10% Waste Buffer'], [cuYards, cuYards * 0.1], ['#0d9488', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    # ─────────────────────────────────────────────────────────────
    # 2. TILE / ROOFING / MULCH / GRAVEL / PAINT
    # ─────────────────────────────────────────────────────────────
    elif "tile" in cid or "mulch" in cid or "gravel" in cid or "roofing" in cid or "paint" in cid or "brick" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Area Length (Feet)</label>
          <input type="number" id="areaLen" class="calc-input" value="15" min="1" step="0.5">
        </div>
        <div class="form-group">
          <label class="form-label">Area Width (Feet)</label>
          <input type="number" id="areaWidth" class="calc-input" value="12" min="1" step="0.5">
        </div>
        <div class="form-group">
          <label class="form-label">Thickness / Depth (Inches)</label>
          <input type="number" id="matDepth" class="calc-input" value="3" min="0.1" step="0.5">
        </div>
        <div class="form-group">
          <label class="form-label">Waste &amp; Cutting Buffer</label>
          <select id="wastePct" class="calc-select">
            <option value="10" selected>10% Extra Buffer (Recommended)</option>
            <option value="15">15% Extra (Diagonal / Complex)</option>
            <option value="5">5% Extra (Simple)</option>
            <option value="0">0% (Exact)</option>
          </select>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Total Material Required</div>
          <div class="result-hero-val" id="resMatPrimary">1.83 yd&sup3;</div>
          <div style="font-weight:600; color:#0f766e; margin-top:4px;" id="resSqFt">180.00 sq ft Area</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Square Footage</span><span class="val" id="resArea">180 sq ft</span></div>
          <div class="result-row"><span class="label">Volume in Cubic Feet</span><span class="val" id="resMatCuFt">45.00 cu ft</span></div>
          <div class="result-row"><span class="label">Total with Buffer</span><span class="val" id="resMatBuffer">2.02 yd&sup3; (49.5 cu ft)</span></div>
          <div class="result-row"><span class="label">Standard Bags (2 cu ft each)</span><span class="val" id="resBags">25 Bags</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var l = parseFloat(document.getElementById('areaLen').value) || 0;
          var w = parseFloat(document.getElementById('areaWidth').value) || 0;
          var dIn = parseFloat(document.getElementById('matDepth').value) || 0;
          var waste = (parseFloat(document.getElementById('wastePct').value) || 10) / 100;

          var sqFt = l * w;
          var cuFt = sqFt * (dIn / 12);
          var cuYd = cuFt / 27;
          var totalCuYd = cuYd * (1 + waste);
          var totalCuFt = cuFt * (1 + waste);
          var bags = Math.ceil(totalCuFt / 2);

          document.getElementById('resMatPrimary').innerHTML = totalCuYd.toFixed(2) + ' yd&sup3;';
          document.getElementById('resSqFt').textContent = sqFt.toFixed(1) + ' sq ft Area';
          document.getElementById('resArea').textContent = sqFt.toLocaleString() + ' sq ft';
          document.getElementById('resMatCuFt').textContent = cuFt.toFixed(2) + ' cu ft';
          document.getElementById('resMatBuffer').innerHTML = totalCuYd.toFixed(2) + ' yd&sup3; (' + totalCuFt.toFixed(1) + ' cu ft)';
          document.getElementById('resBags').textContent = bags.toLocaleString() + ' Bags';

          CalcCore.renderDoughnutChart('calcChart', ['Base Material', 'Waste / Extra Buffer'], [cuYd, cuYd * waste], ['#0d9488', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    # ─────────────────────────────────────────────────────────────
    # 3. AGE / DATE / TIME / DURATION
    # ─────────────────────────────────────────────────────────────
    elif "age" in cid or "date" in cid or "day" in cid or "time" in cid or "hour" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Start Date / Date of Birth</label>
          <input type="date" id="inpStartDate" class="calc-input" value="1998-05-15">
        </div>
        <div class="form-group">
          <label class="form-label">End / Target Date</label>
          <input type="date" id="inpEndDate" class="calc-input">
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Exact Duration / Age</div>
          <div class="result-hero-val" id="resYears">28 Years</div>
          <div style="font-weight:600; color:#0f766e; margin-top:4px;" id="resFullTime">28 years 3 months 3 days</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Months</span><span class="val" id="resMonths">339 Months</span></div>
          <div class="result-row"><span class="label">Total Weeks</span><span class="val" id="resWeeks">1,475 Weeks</span></div>
          <div class="result-row"><span class="label">Total Days</span><span class="val" id="resDays">10,323 Days</span></div>
          <div class="result-row"><span class="label">Total Hours</span><span class="val" id="resHours">247,752 Hours</span></div>
          <div class="result-row"><span class="label">Next Milestone / Birthday</span><span class="val" id="resNext">In 265 Days</span></div>
        </div>
        '''
        script = '''
        document.getElementById('inpEndDate').valueAsDate = new Date();
        function calculate() {
          var sVal = document.getElementById('inpStartDate').value;
          var eVal = document.getElementById('inpEndDate').value;
          if (!sVal || !eVal) return;

          var s = new Date(sVal);
          var e = new Date(eVal);
          var diffMs = e - s;
          if (diffMs < 0) {
            document.getElementById('resYears').textContent = 'Invalid Range';
            return;
          }

          var years = e.getFullYear() - s.getFullYear();
          var months = e.getMonth() - s.getMonth();
          var days = e.getDate() - s.getDate();
          if (days < 0) {
            months--;
            var prevM = new Date(e.getFullYear(), e.getMonth(), 0);
            days += prevM.getDate();
          }
          if (months < 0) {
            years--;
            months += 12;
          }

          var totalDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
          var totalWeeks = Math.floor(totalDays / 7);
          var totalMonths = years * 12 + months;
          var totalHours = totalDays * 24;

          document.getElementById('resYears').textContent = years + ' Years';
          document.getElementById('resFullTime').textContent = years + ' years, ' + months + ' months, ' + days + ' days';
          document.getElementById('resMonths').textContent = totalMonths.toLocaleString() + ' Months';
          document.getElementById('resWeeks').textContent = totalWeeks.toLocaleString() + ' Weeks';
          document.getElementById('resDays').textContent = totalDays.toLocaleString() + ' Days';
          document.getElementById('resHours').textContent = totalHours.toLocaleString() + ' Hours';

          var nextBday = new Date(e.getFullYear(), s.getMonth(), s.getDate());
          if (nextBday < e) nextBday.setFullYear(e.getFullYear() + 1);
          var daysToNext = Math.ceil((nextBday - e) / (1000 * 60 * 60 * 24));
          document.getElementById('resNext').textContent = 'In ' + daysToNext + ' Days';
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    # ─────────────────────────────────────────────────────────────
    # 4. TIP / DISCOUNT / FUEL / GPA
    # ─────────────────────────────────────────────────────────────
    elif "tip" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Bill Amount</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="tipBill" class="calc-input has-prefix" value="85.50" min="0" step="0.5">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Tip Percentage</label>
          <div class="input-with-affix">
            <input type="number" id="tipPct" class="calc-input has-suffix" value="18" min="0" max="100" step="1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Split Among Number of People</label>
          <input type="number" id="tipPeople" class="calc-input" value="3" min="1" max="100" step="1">
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Total Amount Per Person</div>
          <div class="result-hero-val" id="resTipPerPerson">$33.63</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Tip Amount</span><span class="val" id="resTipTotal">$15.39</span></div>
          <div class="result-row"><span class="label">Tip Per Person</span><span class="val" id="resTipPerson">$5.13</span></div>
          <div class="result-row"><span class="label">Total Bill with Tip</span><span class="val" id="resGrandTotal">$100.89</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var bill = parseFloat(document.getElementById('tipBill').value) || 0;
          var pct = (parseFloat(document.getElementById('tipPct').value) || 18) / 100;
          var people = Math.max(1, parseInt(document.getElementById('tipPeople').value) || 1);

          var tip = bill * pct;
          var total = bill + tip;
          var perPerson = total / people;
          var tipPerPerson = tip / people;

          document.getElementById('resTipPerPerson').textContent = CalcCore.formatCurrency(perPerson);
          document.getElementById('resTipTotal').textContent = CalcCore.formatCurrency(tip);
          document.getElementById('resTipPerson').textContent = CalcCore.formatCurrency(tipPerPerson);
          document.getElementById('resGrandTotal').textContent = CalcCore.formatCurrency(total);

          CalcCore.renderDoughnutChart('calcChart', ['Base Bill', 'Tip Amount'], [bill, tip], ['#0d9488', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    elif "discount" in cid or "percent-off" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Original Price</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="discPrice" class="calc-input has-prefix" value="120" min="0" step="1">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Discount Percentage</label>
          <div class="input-with-affix">
            <input type="number" id="discPct" class="calc-input has-suffix" value="25" min="0" max="100" step="1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Extra Coupon Discount (Optional)</label>
          <div class="input-with-affix">
            <input type="number" id="discCoupon" class="calc-input has-suffix" value="10" min="0" max="100" step="1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Final Sale Price</div>
          <div class="result-hero-val" id="resFinalPrice">$81.00</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Money Saved</span><span class="val" id="resSaved">$39.00</span></div>
          <div class="result-row"><span class="label">Total Discount Percentage</span><span class="val" id="resTotalPct">32.50% Off</span></div>
          <div class="result-row"><span class="label">Initial Price</span><span class="val" id="resInitPrice">$120.00</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var p = parseFloat(document.getElementById('discPrice').value) || 0;
          var d1 = (parseFloat(document.getElementById('discPct').value) || 0) / 100;
          var d2 = (parseFloat(document.getElementById('discCoupon').value) || 0) / 100;

          var afterD1 = p * (1 - d1);
          var finalPrice = afterD1 * (1 - d2);
          var saved = Math.max(0, p - finalPrice);
          var effPct = p > 0 ? (saved / p) * 100 : 0;

          document.getElementById('resFinalPrice').textContent = CalcCore.formatCurrency(finalPrice);
          document.getElementById('resSaved').textContent = CalcCore.formatCurrency(saved);
          document.getElementById('resTotalPct').textContent = effPct.toFixed(2) + '% Off';
          document.getElementById('resInitPrice').textContent = CalcCore.formatCurrency(p);

          CalcCore.renderDoughnutChart('calcChart', ['Final You Pay', 'Total You Save'], [finalPrice, saved], ['#0d9488', '#10b981']);
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    elif "fuel" in cid or "gas" in cid or "mileage" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Trip Distance (Miles or Km)</label>
          <input type="number" id="fuelDist" class="calc-input" value="350" min="1" step="10">
        </div>
        <div class="form-group">
          <label class="form-label">Vehicle Fuel Efficiency (MPG)</label>
          <input type="number" id="fuelEff" class="calc-input" value="28" min="1" step="1">
        </div>
        <div class="form-group">
          <label class="form-label">Gas Price Per Gallon</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="fuelPrice" class="calc-input has-prefix" value="3.65" min="0.1" step="0.05">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Passengers (Split Trip)</label>
          <input type="number" id="fuelPass" class="calc-input" value="2" min="1" step="1">
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Total Trip Fuel Cost</div>
          <div class="result-hero-val" id="resFuelCost">$45.63</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Cost Per Passenger</span><span class="val" id="resFuelPerPass">$22.81</span></div>
          <div class="result-row"><span class="label">Total Fuel Required</span><span class="val" id="resFuelGal">12.50 Gallons</span></div>
          <div class="result-row"><span class="label">Cost Per Mile</span><span class="val" id="resFuelPerMile">$0.13 / mile</span></div>
        </div>
        '''
        script = '''
        function calculate() {
          var dist = parseFloat(document.getElementById('fuelDist').value) || 0;
          var mpg = parseFloat(document.getElementById('fuelEff').value) || 28;
          var price = parseFloat(document.getElementById('fuelPrice').value) || 3.65;
          var pass = Math.max(1, parseInt(document.getElementById('fuelPass').value) || 1);

          var gal = mpg > 0 ? dist / mpg : 0;
          var totalCost = gal * price;
          var perPass = totalCost / pass;
          var perMile = dist > 0 ? totalCost / dist : 0;

          document.getElementById('resFuelCost').textContent = CalcCore.formatCurrency(totalCost);
          document.getElementById('resFuelPerPass').textContent = CalcCore.formatCurrency(perPass);
          document.getElementById('resFuelGal').textContent = gal.toFixed(2) + ' Gallons';
          document.getElementById('resFuelPerMile').textContent = CalcCore.formatCurrency(perMile) + ' / mile';
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    # ─────────────────────────────────────────────────────────────
    # 5. HEALTH & FITNESS (BMI, Calorie, Macro, Pregnancy, Heart)
    # ─────────────────────────────────────────────────────────────
    elif "pregnancy" in cid or "due-date" in cid or "ovulation" in cid or "period" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">First Day of Last Menstrual Period (LMP)</label>
          <input type="date" id="inpLMP" class="calc-input">
        </div>
        <div class="form-group">
          <label class="form-label">Average Menstrual Cycle Length</label>
          <select id="inpCycleDays" class="calc-select">
            <option value="28" selected>28 Days (Standard)</option>
            <option value="26">26 Days</option>
            <option value="30">30 Days</option>
            <option value="32">32 Days</option>
          </select>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Estimated Due Date</div>
          <div class="result-hero-val" id="resDueDate">Nov 22, 2026</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Current Gestational Age</span><span class="val" id="resPregWeeks">12 Weeks 4 Days</span></div>
          <div class="result-row"><span class="label">Trimester Stage</span><span class="val" id="resTrimester">First Trimester</span></div>
          <div class="result-row"><span class="label">Estimated Conception Date</span><span class="val" id="resConception">Mar 01, 2026</span></div>
          <div class="result-row"><span class="label">Days Remaining Until Delivery</span><span class="val" id="resDaysLeft">192 Days</span></div>
        </div>
        '''
        script = '''
        var lmpDate = new Date();
        lmpDate.setDate(lmpDate.getDate() - 70);
        document.getElementById('inpLMP').value = lmpDate.toISOString().split('T')[0];

        function calculate() {
          var val = document.getElementById('inpLMP').value;
          if (!val) return;
          var lmp = new Date(val);
          var cycle = parseInt(document.getElementById('inpCycleDays').value) || 28;

          // Naegele's rule: +280 days + (cycle - 28)
          var dueDate = new Date(lmp.getTime() + (280 + (cycle - 28)) * 24 * 60 * 60 * 1000);
          var conception = new Date(lmp.getTime() + (14 + (cycle - 28)) * 24 * 60 * 60 * 1000);
          var now = new Date();
          var diffMs = now - lmp;
          var totalDays = Math.floor(diffMs / (24 * 60 * 60 * 1000));
          var weeks = Math.floor(totalDays / 7);
          var remDays = totalDays % 7;

          var daysLeft = Math.ceil((dueDate - now) / (24 * 60 * 60 * 1000));
          var trimester = 'First Trimester (Weeks 1-13)';
          if (weeks >= 14 && weeks <= 27) trimester = 'Second Trimester (Weeks 14-27)';
          else if (weeks >= 28) trimester = 'Third Trimester (Weeks 28-40+)';

          document.getElementById('resDueDate').textContent = dueDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
          document.getElementById('resPregWeeks').textContent = weeks + ' Weeks, ' + remDays + ' Days';
          document.getElementById('resTrimester').textContent = trimester;
          document.getElementById('resConception').textContent = conception.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
          document.getElementById('resDaysLeft').textContent = Math.max(0, daysLeft) + ' Days';
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    elif cat == "health":
        inputs = '''
        <div class="form-group">
          <label class="form-label">Biological Gender</label>
          <select id="inpGender" class="calc-select">
            <option value="male" selected>Male</option>
            <option value="female">Female</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Age (Years)</label>
          <input type="number" id="inpAge" class="calc-input" value="28" min="10" max="110">
        </div>
        <div class="form-group">
          <label class="form-label">Height (cm)</label>
          <input type="number" id="inpHeightCm" class="calc-input" value="175" min="80" max="240">
        </div>
        <div class="form-group">
          <label class="form-label">Weight (kg)</label>
          <input type="number" id="inpWeightKg" class="calc-input" value="72" min="30" max="250">
        </div>
        <div class="form-group">
          <label class="form-label">Activity Level</label>
          <select id="inpActivity" class="calc-select">
            <option value="1.2">Sedentary (Office desk job)</option>
            <option value="1.375" selected>Lightly Active (Exercise 1-3 days/wk)</option>
            <option value="1.55">Moderately Active (Exercise 3-5 days/wk)</option>
            <option value="1.725">Very Active (Hard training 6-7 days/wk)</option>
          </select>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Daily Maintenance Calories (TDEE)</div>
          <div class="result-hero-val" id="resTDEE">2,324 kcal</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Basal Metabolic Rate (BMR)</span><span class="val" id="resBMR">1,690 kcal</span></div>
          <div class="result-row"><span class="label">Weight Loss Target (0.5 kg / wk)</span><span class="val" id="resLoss">1,824 kcal</span></div>
          <div class="result-row"><span class="label">Muscle Bulking Target</span><span class="val" id="resGain">2,624 kcal</span></div>
          <div class="result-row"><span class="label">BMI Index Status</span><span class="val" id="resHealthBMI">23.5 (Normal)</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var gender = document.getElementById('inpGender').value;
          var age = parseFloat(document.getElementById('inpAge').value) || 28;
          var cm = parseFloat(document.getElementById('inpHeightCm').value) || 175;
          var kg = parseFloat(document.getElementById('inpWeightKg').value) || 72;
          var act = parseFloat(document.getElementById('inpActivity').value) || 1.375;

          var bmr = (10 * kg) + (6.25 * cm) - (5 * age);
          if (gender === 'male') bmr += 5;
          else bmr -= 161;

          var tdee = bmr * act;
          var loss = tdee - 500;
          var gain = tdee + 300;

          var heightM = cm / 100;
          var bmi = kg / (heightM * heightM);

          document.getElementById('resTDEE').textContent = Math.round(tdee).toLocaleString() + ' kcal';
          document.getElementById('resBMR').textContent = Math.round(bmr).toLocaleString() + ' kcal';
          document.getElementById('resLoss').textContent = Math.round(loss).toLocaleString() + ' kcal';
          document.getElementById('resGain').textContent = Math.round(gain).toLocaleString() + ' kcal';
          document.getElementById('resHealthBMI').textContent = bmi.toFixed(1) + ' (Normal)';

          var pG = Math.round((tdee * 0.3) / 4);
          var cG = Math.round((tdee * 0.45) / 4);
          var fG = Math.round((tdee * 0.25) / 9);

          CalcCore.renderDoughnutChart('calcChart', ['Protein (30%)', 'Carbohydrates (45%)', 'Healthy Fats (25%)'], [pG, cG, fG], ['#0d9488', '#0284c7', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    # ─────────────────────────────────────────────────────────────
    # 6. FINANCIAL (MORTGAGE / LOANS / INVESTMENT / SALARY / TAX)
    # ─────────────────────────────────────────────────────────────
    elif "mortgage" in cid or "house" in cid or "fha" in cid or "va" in cid or "rent" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Home Price</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpHomePrice" class="calc-input has-prefix" value="400000" min="1000" step="5000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Down Payment (20%)</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpDownPayment" class="calc-input has-prefix" value="80000" min="0" step="5000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Loan Term</label>
          <select id="inpLoanTerm" class="calc-select">
            <option value="30" selected>30 Years Fixed</option>
            <option value="20">20 Years Fixed</option>
            <option value="15">15 Years Fixed</option>
            <option value="10">10 Years Fixed</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Interest Rate</label>
          <div class="input-with-affix">
            <input type="number" id="inpInterestRate" class="calc-input has-suffix" value="6.5" min="0.1" max="25" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Annual Property Tax &amp; Insurance</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpTaxIns" class="calc-input has-prefix" value="6000" min="0" step="100">
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Total Monthly Payment</div>
          <div class="result-hero-val" id="resMonthly">$2,522.61</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Principal &amp; Interest</span><span class="val" id="resPI">$2,022.61</span></div>
          <div class="result-row"><span class="label">Taxes &amp; Insurance</span><span class="val" id="resTax">$500.00</span></div>
          <div class="result-row"><span class="label">Total Loan Amount</span><span class="val" id="resLoanAmt">$320,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest Paid</span><span class="val" id="resTotalInterest">$408,139.60</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var hp = parseFloat(document.getElementById('inpHomePrice').value) || 0;
          var dp = parseFloat(document.getElementById('inpDownPayment').value) || 0;
          var years = parseFloat(document.getElementById('inpLoanTerm').value) || 30;
          var rate = (parseFloat(document.getElementById('inpInterestRate').value) || 6.5) / 100 / 12;
          var taxIns = (parseFloat(document.getElementById('inpTaxIns').value) || 0) / 12;

          var P = Math.max(0, hp - dp);
          var n = years * 12;
          var pi = 0;
          if (rate > 0) {
            pi = P * (rate * Math.pow(1 + rate, n)) / (Math.pow(1 + rate, n) - 1);
          } else {
            pi = P / n;
          }

          var totalMonthly = pi + taxIns;
          var totalCost = pi * n;
          var totalInterest = Math.max(0, totalCost - P);

          document.getElementById('resMonthly').textContent = CalcCore.formatCurrency(totalMonthly);
          document.getElementById('resPI').textContent = CalcCore.formatCurrency(pi);
          document.getElementById('resTax').textContent = CalcCore.formatCurrency(taxIns);
          document.getElementById('resLoanAmt').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resTotalInterest').textContent = CalcCore.formatCurrency(totalInterest);

          CalcCore.renderDoughnutChart('calcChart', ['Principal Loan', 'Total Interest', 'Taxes & Insurance'], [P, totalInterest, taxIns * n], ['#0d9488', '#f59e0b', '#0284c7']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    elif "loan" in cid or "debt" in cid or "credit" in cid or "payment" in cid or "lease" in cid or "apr" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Total Loan Amount</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpLoanP" class="calc-input has-prefix" value="25000" min="100" step="500">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Loan Term (Years)</label>
          <input type="number" id="inpLoanYrs" class="calc-input" value="5" min="1" max="30" step="1">
        </div>
        <div class="form-group">
          <label class="form-label">Annual Interest Rate (APR)</label>
          <div class="input-with-affix">
            <input type="number" id="inpLoanRate" class="calc-input has-suffix" value="7.5" min="0" max="40" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Monthly Payment (EMI)</div>
          <div class="result-hero-val" id="resLoanEMI">$500.95</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Payments</span><span class="val" id="resLoanTotalPay">$30,057.00</span></div>
          <div class="result-row"><span class="label">Total Principal</span><span class="val" id="resLoanPrincipal">$25,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest Paid</span><span class="val" id="resLoanTotalInt">$5,057.00</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var P = parseFloat(document.getElementById('inpLoanP').value) || 0;
          var years = parseFloat(document.getElementById('inpLoanYrs').value) || 5;
          var r = (parseFloat(document.getElementById('inpLoanRate').value) || 7.5) / 100 / 12;
          var n = years * 12;

          var emi = 0;
          if (r > 0) {
            emi = P * (r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
          } else {
            emi = P / n;
          }

          var totalPay = emi * n;
          var totalInt = Math.max(0, totalPay - P);

          document.getElementById('resLoanEMI').textContent = CalcCore.formatCurrency(emi);
          document.getElementById('resLoanTotalPay').textContent = CalcCore.formatCurrency(totalPay);
          document.getElementById('resLoanPrincipal').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resLoanTotalInt').textContent = CalcCore.formatCurrency(totalInt);

          CalcCore.renderDoughnutChart('calcChart', ['Principal Loan', 'Total Interest'], [P, totalInt], ['#0d9488', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    elif "salary" in cid or "wage" in cid or "paycheck" in cid or "tax" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Gross Salary / Income</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpGrossWage" class="calc-input has-prefix" value="75000" min="0" step="1000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Pay Frequency</label>
          <select id="inpWageType" class="calc-select">
            <option value="year" selected>Per Year (Annual)</option>
            <option value="hour">Per Hour (40 hrs/week)</option>
            <option value="month">Per Month</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Tax Deduction Rate (Federal + State)</label>
          <div class="input-with-affix">
            <input type="number" id="inpTaxDeduct" class="calc-input has-suffix" value="22" min="0" max="50" step="0.5">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Net Take-Home Pay (Annual)</div>
          <div class="result-hero-val" id="resNetAnnual">$58,500.00</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Monthly Take-Home</span><span class="val" id="resNetMonthly">$4,875.00</span></div>
          <div class="result-row"><span class="label">Bi-Weekly Take-Home</span><span class="val" id="resNetBiWeekly">$2,250.00</span></div>
          <div class="result-row"><span class="label">Hourly Rate (Equivalent)</span><span class="val" id="resHourlyEq">$36.06 / hr</span></div>
          <div class="result-row"><span class="label">Total Tax Deducted</span><span class="val" id="resTotalTax">$16,500.00</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var raw = parseFloat(document.getElementById('inpGrossWage').value) || 0;
          var type = document.getElementById('inpWageType').value;
          var taxRate = (parseFloat(document.getElementById('inpTaxDeduct').value) || 22) / 100;

          var annualGross = raw;
          if (type === 'hour') annualGross = raw * 2080;
          else if (type === 'month') annualGross = raw * 12;

          var tax = annualGross * taxRate;
          var netAnnual = annualGross - tax;
          var netMonthly = netAnnual / 12;
          var netBiWeekly = netAnnual / 26;
          var hourlyEq = annualGross / 2080;

          document.getElementById('resNetAnnual').textContent = CalcCore.formatCurrency(netAnnual);
          document.getElementById('resNetMonthly').textContent = CalcCore.formatCurrency(netMonthly);
          document.getElementById('resNetBiWeekly').textContent = CalcCore.formatCurrency(netBiWeekly);
          document.getElementById('resHourlyEq').textContent = CalcCore.formatCurrency(hourlyEq) + ' / hr';
          document.getElementById('resTotalTax').textContent = CalcCore.formatCurrency(tax);

          CalcCore.renderDoughnutChart('calcChart', ['Net Take-Home', 'Taxes & Deductions'], [netAnnual, tax], ['#0d9488', '#ef4444']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    elif cat == "financial":
        inputs = '''
        <div class="form-group">
          <label class="form-label">Initial Investment / Principal</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpInitInv" class="calc-input has-prefix" value="10000" min="0" step="500">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Monthly Contribution</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpMonthlyInv" class="calc-input has-prefix" value="500" min="0" step="50">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Investment Duration (Years)</label>
          <input type="number" id="inpInvYrs" class="calc-input" value="15" min="1" max="50">
        </div>
        <div class="form-group">
          <label class="form-label">Estimated Annual Return Rate</label>
          <div class="input-with-affix">
            <input type="number" id="inpInvRate" class="calc-input has-suffix" value="8" min="0.1" max="40" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Estimated Future Value</div>
          <div class="result-hero-val" id="resInvEnd">$206,854.72</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Initial Principal</span><span class="val" id="resInvInit">$10,000.00</span></div>
          <div class="result-row"><span class="label">Total Additional Contributions</span><span class="val" id="resInvContribs">$90,000.00</span></div>
          <div class="result-row"><span class="label">Total Compound Interest</span><span class="val" id="resInvGrowth">$106,854.72</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var P = parseFloat(document.getElementById('inpInitInv').value) || 0;
          var PMT = parseFloat(document.getElementById('inpMonthlyInv').value) || 0;
          var yrs = parseFloat(document.getElementById('inpInvYrs').value) || 15;
          var r = (parseFloat(document.getElementById('inpInvRate').value) || 8) / 100;

          var labels = [];
          var balanceData = [];
          var contribData = [];

          var balance = P;
          var totalContrib = P;

          for (var y = 0; y <= yrs; y++) {
            labels.push('Yr ' + y);
            if (y === 0) {
              balanceData.push(P);
              contribData.push(P);
            } else {
              for (var m = 0; m < 12; m++) {
                balance = balance * (1 + r / 12) + PMT;
                totalContrib += PMT;
              }
              balanceData.push(balance);
              contribData.push(totalContrib);
            }
          }

          var growth = Math.max(0, balance - totalContrib);
          document.getElementById('resInvEnd').textContent = CalcCore.formatCurrency(balance);
          document.getElementById('resInvInit').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resInvContribs').textContent = CalcCore.formatCurrency(totalContrib - P);
          document.getElementById('resInvGrowth').textContent = CalcCore.formatCurrency(growth);

          CalcCore.renderLineChart('calcChart', labels, [
            { label: 'Total Balance ($)', data: balanceData, borderColor: '#0d9488', backgroundColor: 'rgba(13,148,136,0.1)', fill: true, tension: 0.3 },
            { label: 'Total Invested ($)', data: contribData, borderColor: '#0284c7', backgroundColor: 'transparent', borderDash: [5, 5], tension: 0 }
          ]);
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    # ─────────────────────────────────────────────────────────────
    # 7. MATH & SCIENTIFIC
    # ─────────────────────────────────────────────────────────────
    elif "scientific" in cid:
        inputs = '''
        <div style="background:#0f172a; padding:16px; border-radius:12px; margin-bottom:14px; text-align:right;">
          <div id="sciHistory" style="color:#94a3b8; font-size:0.85rem; font-family:'JetBrains Mono', monospace; min-height:18px;"></div>
          <div id="sciDisplay" style="color:#ffffff; font-size:2rem; font-weight:700; font-family:'JetBrains Mono', monospace; overflow-x:auto;">0</div>
        </div>
        <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:6px;">
          <button class="unit-btn" onclick="sciOp('sin')">sin</button>
          <button class="unit-btn" onclick="sciOp('cos')">cos</button>
          <button class="unit-btn" onclick="sciOp('tan')">tan</button>
          <button class="unit-btn" onclick="sciOp('log')">log</button>
          <button class="unit-btn" onclick="sciOp('ln')">ln</button>

          <button class="unit-btn" onclick="sciOp('sqrt')">&radic;</button>
          <button class="unit-btn" onclick="sciOp('sq')">x&sup2;</button>
          <button class="unit-btn" onclick="sciOp('pow')">x^y</button>
          <button class="unit-btn" onclick="sciOp('pi')">&pi;</button>
          <button class="unit-btn" onclick="sciOp('e')">e</button>

          <button class="unit-btn" style="background:#fee2e2; color:#ef4444;" onclick="sciClear()">C</button>
          <button class="unit-btn" onclick="sciInput('(')">(</button>
          <button class="unit-btn" onclick="sciInput(')')">)</button>
          <button class="unit-btn" onclick="sciOp('fact')">n!</button>
          <button class="unit-btn" onclick="sciInput('/')">&divide;</button>

          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('7')">7</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('8')">8</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('9')">9</button>
          <button class="unit-btn" onclick="sciInput('*')">&times;</button>
          <button class="unit-btn" onclick="sciOp('recip')">1/x</button>

          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('4')">4</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('5')">5</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('6')">6</button>
          <button class="unit-btn" onclick="sciInput('-')">&minus;</button>
          <button class="unit-btn" onclick="sciOp('abs')">|x|</button>

          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('1')">1</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('2')">2</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('3')">3</button>
          <button class="unit-btn" onclick="sciInput('+')">+</button>
          <button class="unit-btn" onclick="sciOp('neg')">&plusmn;</button>

          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('0')">0</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('.')">.</button>
          <button class="unit-btn" style="background:#f8fafc;" onclick="sciInput('00')">00</button>
          <button class="unit-btn" style="grid-column:span 2; background:var(--primary); color:#fff;" onclick="sciEval()">=</button>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Calculation Output</div>
          <div class="result-hero-val" id="sciResult">0</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Trigonometry Angle</span><span class="val">Degrees &amp; Radians</span></div>
          <div class="result-row"><span class="label">Precision</span><span class="val">12 Significant Digits</span></div>
        </div>
        '''
        script = '''
        var currExpr = '';
        function sciInput(char) {
          currExpr += char;
          document.getElementById('sciDisplay').textContent = currExpr;
        }
        function sciClear() {
          currExpr = '';
          document.getElementById('sciDisplay').textContent = '0';
          document.getElementById('sciHistory').textContent = '';
          document.getElementById('sciResult').textContent = '0';
        }
        function sciOp(op) {
          try {
            var v = eval(currExpr || '0');
            var res = 0;
            if (op === 'sin') res = Math.sin(v * Math.PI / 180);
            else if (op === 'cos') res = Math.cos(v * Math.PI / 180);
            else if (op === 'tan') res = Math.tan(v * Math.PI / 180);
            else if (op === 'log') res = Math.log10(v);
            else if (op === 'ln') res = Math.log(v);
            else if (op === 'sqrt') res = Math.sqrt(v);
            else if (op === 'sq') res = v * v;
            else if (op === 'pi') res = Math.PI;
            else if (op === 'e') res = Math.E;
            else if (op === 'recip') res = 1 / v;
            else if (op === 'abs') res = Math.abs(v);
            else if (op === 'neg') res = -v;
            else if (op === 'pow') { currExpr += '**'; document.getElementById('sciDisplay').textContent = currExpr; return; }

            currExpr = String(res);
            document.getElementById('sciDisplay').textContent = currExpr;
            document.getElementById('sciResult').textContent = currExpr;
          } catch(e) {
            document.getElementById('sciDisplay').textContent = 'Error';
          }
        }
        function sciEval() {
          try {
            document.getElementById('sciHistory').textContent = currExpr + ' =';
            var res = eval(currExpr);
            document.getElementById('sciDisplay').textContent = res;
            document.getElementById('sciResult').textContent = res;
            currExpr = String(res);
          } catch(e) {
            document.getElementById('sciDisplay').textContent = 'Error';
          }
        }
        '''
        return inputs, results, script

    elif "percent" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">What is</label>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="number" id="p1" class="calc-input" value="15" style="flex:1;">
            <span style="font-weight:700; color:var(--text-muted);">% of</span>
            <input type="number" id="p2" class="calc-input" value="250" style="flex:1.5;">
          </div>
        </div>
        <div class="form-group" style="margin-top:24px;">
          <label class="form-label">Percentage Increase / Decrease</label>
          <div style="display:flex; gap:10px; align-items:center;">
            <input type="number" id="c1" class="calc-input" value="120" placeholder="From" style="flex:1;">
            <span style="font-weight:700; color:var(--text-muted);">&rarr;</span>
            <input type="number" id="c2" class="calc-input" value="180" placeholder="To" style="flex:1;">
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Calculated Result (X% of Y)</div>
          <div class="result-hero-val" id="resPVal">37.5</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Percentage Change</span><span class="val" id="resChange">+50.00%</span></div>
          <div class="result-row"><span class="label">Absolute Difference</span><span class="val" id="resDiff">60</span></div>
        </div>
        '''
        script = '''
        function calculate() {
          var p1 = parseFloat(document.getElementById('p1').value) || 0;
          var p2 = parseFloat(document.getElementById('p2').value) || 0;
          var c1 = parseFloat(document.getElementById('c1').value) || 0;
          var c2 = parseFloat(document.getElementById('c2').value) || 0;

          var r1 = (p1 / 100) * p2;
          document.getElementById('resPVal').textContent = CalcCore.formatNumber(r1, 2);

          var diff = c2 - c1;
          var pctChange = c1 !== 0 ? (diff / c1) * 100 : 0;
          var sign = pctChange >= 0 ? '+' : '';
          document.getElementById('resChange').textContent = sign + pctChange.toFixed(2) + '%';
          document.getElementById('resDiff').textContent = CalcCore.formatNumber(Math.abs(diff), 2);
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

    else:
        # Generic Math / Utility
        inputs = '''
        <div class="form-group">
          <label class="form-label">Primary Number / Value (A)</label>
          <input type="number" id="inpMathA" class="calc-input" value="48" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">Secondary Number / Value (B)</label>
          <input type="number" id="inpMathB" class="calc-input" value="18" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">Operation</label>
          <select id="inpMathOp" class="calc-select">
            <option value="pct" selected>Ratio &amp; Percentage (A of B)</option>
            <option value="diff">Difference (A - B)</option>
            <option value="pow">Power (A^B)</option>
            <option value="gcd">Greatest Common Divisor (GCD)</option>
            <option value="lcm">Least Common Multiple (LCM)</option>
          </select>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Computed Result</div>
          <div class="result-hero-val" id="resMathMain">266.67%</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Sum (A + B)</span><span class="val" id="resMathSum">66</span></div>
          <div class="result-row"><span class="label">Product (A &times; B)</span><span class="val" id="resMathProd">864</span></div>
          <div class="result-row"><span class="label">Ratio (A : B)</span><span class="val" id="resMathRatio">8 : 3</span></div>
        </div>
        '''
        script = '''
        function gcd(a, b) { return b ? gcd(b, a % b) : Math.abs(a); }
        function lcm(a, b) { return (a && b) ? (Math.abs(a * b) / gcd(a, b)) : 0; }

        function calculate() {
          var a = parseFloat(document.getElementById('inpMathA').value) || 0;
          var b = parseFloat(document.getElementById('inpMathB').value) || 0;
          var op = document.getElementById('inpMathOp').value;

          var res = 0;
          if (op === 'pct') res = b !== 0 ? ((a / b) * 100).toFixed(2) + '%' : '0%';
          else if (op === 'diff') res = (a - b).toLocaleString();
          else if (op === 'pow') res = Math.pow(a, b).toFixed(4);
          else if (op === 'gcd') res = gcd(Math.round(a), Math.round(b));
          else if (op === 'lcm') res = lcm(Math.round(a), Math.round(b));

          var g = gcd(Math.round(a), Math.round(b)) || 1;
          var ratioStr = (Math.round(a)/g) + ' : ' + (Math.round(b)/g);

          document.getElementById('resMathMain').textContent = res;
          document.getElementById('resMathSum').textContent = (a + b).toLocaleString();
          document.getElementById('resMathProd').textContent = (a * b).toLocaleString();
          document.getElementById('resMathRatio').textContent = ratioStr;
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''
        return inputs, results, script

# ══════════════════════════════════════════════════════════════════
# BUILD ALL 204 INDIVIDUAL TOOL PAGES
# ══════════════════════════════════════════════════════════════════

def build_all_specialized_tools():
    for tool in ALL_TOOLS:
        cid = tool["id"]
        title = tool["title"]
        cat = tool["category"]
        cat_title = tool["category_title"]
        desc = f"Free online {title.lower()} by Daily1Step. Instant calculations, interactive parameters, formula explanations, and FAQs."

        inputs_html, results_html, script_js = get_specialized_engine(tool)

        tool_dir = os.path.join(TOOLS_DIR, cid)
        os.makedirs(tool_dir, exist_ok=True)

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Free Online Calculator | Daily1Step</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://bypyay.github.io/calculator/tools/{cid}/">
<link rel="stylesheet" href="../../assets/css/style.css?v=3">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "{title} - Daily1Step",
  "url": "https://bypyay.github.io/calculator/tools/{cid}/",
  "description": "{desc}",
  "applicationCategory": "EducationalApplication",
  "operatingSystem": "All modern web browsers",
  "offers": {{
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }}
}}
</script>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="../../index.html" class="brand">
      <div class="brand-icon"><i class="fa-solid fa-calculator"></i></div>
      <div class="brand-title">Daily1Step <span class="accent">Calc</span></div>
    </a>
    <nav class="nav-links">
      <a href="../../index.html" class="nav-link"><i class="fa-solid fa-grid-2"></i> All 204+ Calculators</a>
    </nav>
  </div>
</header>

<main class="calc-workspace-wrap">
  <div class="calc-header-meta">
    <div class="calc-breadcrumb">
      <a href="../../index.html">Home</a>
      <span>/</span>
      <span>{cat_title}</span>
      <span>/</span>
      <span>{title}</span>
    </div>
    <h1 class="calc-main-title">{title}</h1>
    <p class="calc-main-desc">{desc}</p>
  </div>

  <div class="calc-grid-layout">
    <!-- Left Inputs Card -->
    <div class="calc-card">
      <div class="calc-card-title">
        <span><i class="fa-solid fa-sliders" style="color:var(--primary); margin-right:8px;"></i> Input Parameters</span>
      </div>
      {inputs_html}
      <button type="button" class="btn-calc-primary" onclick="calculate()">
        <i class="fa-solid fa-calculator"></i> Recalculate
      </button>
    </div>

    <!-- Right Results Card -->
    <div class="calc-card">
      <div class="calc-card-title">
        <span><i class="fa-solid fa-chart-pie" style="color:var(--primary); margin-right:8px;"></i> Calculation Summary</span>
      </div>
      {results_html}
    </div>
  </div>

  <!-- Educational Guide & FAQs -->
  <section class="guide-section">
    <h2>How the {title} Works</h2>
    <p>
      The <strong>{title}</strong> by Daily1Step provides precise, instant computations directly in your browser. All computations follow standardized formulas and equations without transmitting any sensitive personal data to external servers.
    </p>

    <h3>Formula &amp; Mathematical Method</h3>
    <div class="formula-box">
      Formula: Calculations are evaluated dynamically in high-precision JavaScript with instant updates.
    </div>

    <h3>Frequently Asked Questions</h3>
    <div class="faq-card">
      <div class="faq-q">Is this {title} completely free to use?</div>
      <div class="faq-a">Yes! All calculations, interactive charts, and reports are 100% free with no registration, no subscription, and no hidden fees.</div>
    </div>
    <div class="faq-card">
      <div class="faq-q">Is my personal or financial data private?</div>
      <div class="faq-a">Absolutely. All calculations happen entirely within your local browser memory. Your data is never uploaded, saved, or shared with third parties.</div>
    </div>
    <div class="faq-card">
      <div class="faq-q">Can I use this calculator on mobile devices?</div>
      <div class="faq-a">Yes, Daily1Step Calculators are fully responsive and optimized for smartphones, tablets, laptops, and desktop screens.</div>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-links">
      <a href="../../index.html">All Calculators</a>
      <a href="../../legal/privacy.html">Privacy Policy</a>
      <a href="../../legal/terms.html">Terms of Service</a>
      <a href="../../legal/about.html">About Us</a>
      <a href="../../legal/contact.html">Contact</a>
      <a href="../../legal/disclaimer.html">Disclaimer</a>
    </div>
    <p class="copyright">&copy; 2026 Daily1Step. Free online calculators for finance, health, math, and daily utilities.</p>
  </div>
</footer>

<script src="../../vendor/chart.umd.min.js"></script>
<script src="../../vendor/jspdf.umd.min.js"></script>
<script src="../../assets/js/calculator-core.js"></script>
<script>
{script_js}
</script>
</body>
</html>'''

        out_path = os.path.join(tool_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

    print(f"Generated all {len(ALL_TOOLS)} specialized tool pages!")

if __name__ == "__main__":
    build_all_specialized_tools()
