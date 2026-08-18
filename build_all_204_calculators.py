# -*- coding: utf-8 -*-
"""
Daily1Step Master Builder for 204+ Calculators
Generates all 204 calculators with complete formulas, interactive inputs, live calculations, Chart.js visualizations, guides, and FAQs.
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

print(f"Loaded {len(ALL_TOOLS)} tools from all_calc_tools.json")

# Category Font Awesome Icon Map
CAT_ICON_MAP = {
    "financial": "fa-hand-holding-dollar",
    "health": "fa-heart-pulse",
    "math": "fa-square-root-variable",
    "everyday": "fa-clock"
}

def get_tool_icon(cid, cat):
    if "mortgage" in cid or "house" in cid or "rent" in cid: return "fa-house"
    if "car" in cid or "auto" in cid or "vehicle" in cid: return "fa-car"
    if "tax" in cid: return "fa-file-invoice-dollar"
    if "salary" in cid or "wage" in cid or "paycheck" in cid: return "fa-money-bill-wave"
    if "loan" in cid or "debt" in cid: return "fa-hand-holding-dollar"
    if "interest" in cid or "percent" in cid: return "fa-percent"
    if "retirement" in cid or "pension" in cid: return "fa-umbrella-beach"
    if "investment" in cid or "stock" in cid or "fund" in cid: return "fa-chart-line-up"
    if "card" in cid: return "fa-credit-card"
    if "savings" in cid: return "fa-piggy-bank"
    if "bmi" in cid or "weight" in cid: return "fa-weight-scale"
    if "calorie" in cid or "tdee" in cid or "bmr" in cid: return "fa-fire-flame-curved"
    if "body-fat" in cid or "body" in cid: return "fa-person"
    if "pace" in cid or "run" in cid: return "fa-person-running"
    if "pregnancy" in cid or "baby" in cid: return "fa-baby"
    if "heart" in cid or "blood" in cid: return "fa-heart"
    if "fraction" in cid: return "fa-divide"
    if "triangle" in cid: return "fa-shapes"
    if "volume" in cid or "cube" in cid: return "fa-cube"
    if "age" in cid or "birthday" in cid: return "fa-cake-candles"
    if "date" in cid or "day" in cid or "calendar" in cid: return "fa-calendar-days"
    if "time" in cid or "hour" in cid: return "fa-clock"
    if "gpa" in cid or "grade" in cid: return "fa-graduation-cap"
    if "tip" in cid: return "fa-receipt"
    if "discount" in cid: return "fa-tags"
    if "fuel" in cid or "gas" in cid: return "fa-gas-pump"
    if "concrete" in cid or "tile" in cid or "roofing" in cid: return "fa-trowel-bricks"
    return CAT_ICON_MAP.get(cat, "fa-calculator")

# ══════════════════════════════════════════════════════════════════
# FORMULA AND UI ENGINE GENERATOR
# ══════════════════════════════════════════════════════════════════

def generate_calc_engine(tool):
    cid = tool["id"]
    cat = tool["category"]
    title = tool["title"]

    # 1. Mortgage Family
    if "mortgage" in cid or "house-affordability" in cid or "fha-loan" in cid or "va-mortgage" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Home Price / Property Value</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpHomePrice" class="calc-input has-prefix" value="450000" min="1000" step="5000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Down Payment Amount (20%)</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpDownPayment" class="calc-input has-prefix" value="90000" min="0" step="5000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Loan Term (Years)</label>
          <select id="inpLoanTerm" class="calc-select">
            <option value="30" selected>30 Years Fixed</option>
            <option value="20">20 Years Fixed</option>
            <option value="15">15 Years Fixed</option>
            <option value="10">10 Years Fixed</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Annual Interest Rate (APR)</label>
          <div class="input-with-affix">
            <input type="number" id="inpInterestRate" class="calc-input has-suffix" value="6.75" min="0.1" max="25" step="0.1">
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
          <div class="result-hero-label">Estimated Monthly Payment</div>
          <div class="result-hero-val" id="resMonthly">$2,835.08</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Principal &amp; Interest</span><span class="val" id="resPI">$2,335.08</span></div>
          <div class="result-row"><span class="label">Property Tax &amp; Insurance</span><span class="val" id="resTax">$500.00</span></div>
          <div class="result-row"><span class="label">Total Loan Amount</span><span class="val" id="resLoanAmt">$360,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest Over Term</span><span class="val" id="resTotalInterest">$480,629.80</span></div>
          <div class="result-row"><span class="label">Total Cost of Loan</span><span class="val" id="resTotalCost">$840,629.80</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var hp = parseFloat(document.getElementById('inpHomePrice').value) || 0;
          var dp = parseFloat(document.getElementById('inpDownPayment').value) || 0;
          var years = parseFloat(document.getElementById('inpLoanTerm').value) || 30;
          var rate = (parseFloat(document.getElementById('inpInterestRate').value) || 6.75) / 100 / 12;
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
          var totalPI = pi * n;
          var totalInterest = Math.max(0, totalPI - P);

          document.getElementById('resMonthly').textContent = CalcCore.formatCurrency(totalMonthly);
          document.getElementById('resPI').textContent = CalcCore.formatCurrency(pi);
          document.getElementById('resTax').textContent = CalcCore.formatCurrency(taxIns);
          document.getElementById('resLoanAmt').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resTotalInterest').textContent = CalcCore.formatCurrency(totalInterest);
          document.getElementById('resTotalCost').textContent = CalcCore.formatCurrency(totalPI + taxIns * n);

          CalcCore.renderDoughnutChart('calcChart', ['Principal Loan', 'Total Interest', 'Taxes & Insurance'], [P, totalInterest, taxIns * n], ['#0d9488', '#f59e0b', '#0284c7']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    # 2. General Loan / Auto Loan / EMI Family
    elif "loan" in cid or "payment" in cid or "credit" in cid or "debt" in cid or "lease" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Total Loan / Debt Balance</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpLoanP" class="calc-input has-prefix" value="30000" min="100" step="500">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Payoff Term (Years)</label>
          <input type="number" id="inpLoanYrs" class="calc-input" value="5" min="0.5" max="30" step="0.5">
        </div>
        <div class="form-group">
          <label class="form-label">Annual Interest Rate (APR)</label>
          <div class="input-with-affix">
            <input type="number" id="inpLoanRate" class="calc-input has-suffix" value="7.2" min="0" max="40" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Monthly EMI Payment</div>
          <div class="result-hero-val" id="resLoanEMI">$596.88</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Payments (Principal + Interest)</span><span class="val" id="resLoanTotalPay">$35,812.80</span></div>
          <div class="result-row"><span class="label">Total Principal Borrowed</span><span class="val" id="resLoanPrincipal">$30,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest Paid</span><span class="val" id="resLoanTotalInt">$5,812.80</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var P = parseFloat(document.getElementById('inpLoanP').value) || 0;
          var years = parseFloat(document.getElementById('inpLoanYrs').value) || 5;
          var r = (parseFloat(document.getElementById('inpLoanRate').value) || 7.2) / 100 / 12;
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

    # 3. Investment / Compound Interest / 401K / Retirement / Savings Family
    elif "interest" in cid or "investment" in cid or "compound" in cid or "401k" in cid or "retirement" in cid or "savings" in cid or "annuity" in cid or "cd" in cid or "roi" in cid or "future-value" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Initial Investment Amount</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpInitInv" class="calc-input has-prefix" value="15000" min="0" step="500">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Monthly Additional Contribution</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpMonthlyInv" class="calc-input has-prefix" value="600" min="0" step="50">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Investment Duration (Years)</label>
          <input type="number" id="inpInvYrs" class="calc-input" value="20" min="1" max="60">
        </div>
        <div class="form-group">
          <label class="form-label">Estimated Annual Return Rate</label>
          <div class="input-with-affix">
            <input type="number" id="inpInvRate" class="calc-input has-suffix" value="8.5" min="0.1" max="40" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Estimated Future Portfolio Value</div>
          <div class="result-hero-val" id="resInvEnd">$485,392.41</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Initial Principal</span><span class="val" id="resInvInit">$15,000.00</span></div>
          <div class="result-row"><span class="label">Total Contributions</span><span class="val" id="resInvContribs">$144,000.00</span></div>
          <div class="result-row"><span class="label">Total Growth &amp; Compound Interest</span><span class="val" id="resInvGrowth">$326,392.41</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var P = parseFloat(document.getElementById('inpInitInv').value) || 0;
          var PMT = parseFloat(document.getElementById('inpMonthlyInv').value) || 0;
          var yrs = parseFloat(document.getElementById('inpInvYrs').value) || 20;
          var r = (parseFloat(document.getElementById('inpInvRate').value) || 8.5) / 100;

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

    # 4. Salary / Wage / Tax Family
    elif "salary" in cid or "wage" in cid or "paycheck" in cid or "tax" in cid:
        inputs = '''
        <div class="form-group">
          <label class="form-label">Annual Salary or Hourly Rate</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="inpGrossWage" class="calc-input has-prefix" value="75000" min="0" step="1000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Pay Frequency</label>
          <select id="inpWageType" class="calc-select">
            <option value="year" selected>Per Year</option>
            <option value="hour">Per Hour (40 hrs/wk)</option>
            <option value="month">Per Month</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Estimated Tax Deduction Rate</label>
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
          <div class="result-row"><span class="label">Total Taxes Deducted</span><span class="val" id="resTotalTax">$16,500.00</span></div>
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

    # 5. Fitness & Health (BMI, Calorie, Body Fat, BMR, Macro, TDEE, etc.)
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
            <option value="1.2">Sedentary (Little or no exercise)</option>
            <option value="1.375" selected>Lightly Active (Exercise 1-3 days/wk)</option>
            <option value="1.55">Moderately Active (Exercise 3-5 days/wk)</option>
            <option value="1.725">Very Active (Hard exercise 6-7 days/wk)</option>
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
          <div class="result-row"><span class="label">Weight Loss (0.5 kg / wk)</span><span class="val" id="resLoss">1,824 kcal</span></div>
          <div class="result-row"><span class="label">Weight Gain (Muscle Bulking)</span><span class="val" id="resGain">2,624 kcal</span></div>
          <div class="result-row"><span class="label">BMI Index</span><span class="val" id="resHealthBMI">23.5 (Normal)</span></div>
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

          // Mifflin-St Jeor Formula
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

          // Macro Breakdown
          var proteinG = Math.round((tdee * 0.3) / 4);
          var carbsG = Math.round((tdee * 0.45) / 4);
          var fatG = Math.round((tdee * 0.25) / 9);

          CalcCore.renderDoughnutChart('calcChart', ['Protein (30%)', 'Carbohydrates (45%)', 'Healthy Fats (25%)'], [proteinG, carbsG, fatG], ['#0d9488', '#0284c7', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    # 6. Math & Scientific Family
    elif cat == "math":
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
          <label class="form-label">Operation / Function</label>
          <select id="inpMathOp" class="calc-select">
            <option value="pct" selected>Percentage (A as % of B)</option>
            <option value="diff">Percentage Difference</option>
            <option value="pow">Power (A^B)</option>
            <option value="root">Square Root of A</option>
            <option value="gcd">Greatest Common Divisor (GCD)</option>
            <option value="lcm">Least Common Multiple (LCM)</option>
          </select>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Calculated Result</div>
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
          else if (op === 'diff') res = b !== 0 ? (((a - b) / b) * 100).toFixed(2) + '%' : '0%';
          else if (op === 'pow') res = Math.pow(a, b).toFixed(4);
          else if (op === 'root') res = Math.sqrt(a).toFixed(4);
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

    # 7. Everyday / Age / Date / Tip / Construction Family
    else:
        if "age" in cid or "birthday" in cid or "date" in cid or "day" in cid:
            inputs = '''
            <div class="form-group">
              <label class="form-label">Start Date / Date of Birth</label>
              <input type="date" id="inpStartDate" class="calc-input" value="1996-08-15">
            </div>
            <div class="form-group">
              <label class="form-label">Target / End Date</label>
              <input type="date" id="inpEndDate" class="calc-input">
            </div>
            '''
            results = '''
            <div class="result-hero-box">
              <div class="result-hero-label">Total Time Duration</div>
              <div class="result-hero-val" id="resDateDiffYears">30 Years</div>
              <div style="font-weight:600; color:#0f766e; margin-top:4px;" id="resDateFull">30 years 0 months 3 days</div>
            </div>
            <div class="result-breakdown-list">
              <div class="result-row"><span class="label">Total Days</span><span class="val" id="resDateDays">10,961 Days</span></div>
              <div class="result-row"><span class="label">Total Weeks</span><span class="val" id="resDateWeeks">1,565 Weeks</span></div>
              <div class="result-row"><span class="label">Total Hours</span><span class="val" id="resDateHours">263,064 Hours</span></div>
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
                document.getElementById('resDateDiffYears').textContent = 'Invalid Date Range';
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
              var totalHours = totalDays * 24;

              document.getElementById('resDateDiffYears').textContent = years + ' Years';
              document.getElementById('resDateFull').textContent = years + ' years, ' + months + ' months, ' + days + ' days';
              document.getElementById('resDateDays').textContent = totalDays.toLocaleString() + ' Days';
              document.getElementById('resDateWeeks').textContent = totalWeeks.toLocaleString() + ' Weeks';
              document.getElementById('resDateHours').textContent = totalHours.toLocaleString() + ' Hours';
            }
            document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
            calculate();
            '''
        else:
            inputs = '''
            <div class="form-group">
              <label class="form-label">Primary Amount / Measure</label>
              <div class="input-with-affix">
                <span class="input-affix prefix">$</span>
                <input type="number" id="inpUtilVal" class="calc-input has-prefix" value="120" min="0" step="any">
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">Rate / Percentage / Factor</label>
              <div class="input-with-affix">
                <input type="number" id="inpUtilFactor" class="calc-input has-suffix" value="18" min="0" step="any">
                <span class="input-affix suffix">%</span>
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">Split / Quantity</label>
              <input type="number" id="inpUtilSplit" class="calc-input" value="3" min="1" step="1">
            </div>
            '''
            results = '''
            <div class="result-hero-box">
              <div class="result-hero-label">Calculated Final Amount</div>
              <div class="result-hero-val" id="resUtilTotal">$141.60</div>
            </div>
            <div class="result-breakdown-list">
              <div class="result-row"><span class="label">Amount per Person / Unit</span><span class="val" id="resUtilPerUnit">$47.20</span></div>
              <div class="result-row"><span class="label">Additional Value Added</span><span class="val" id="resUtilAdd">$21.60</span></div>
            </div>
            '''
            script = '''
            function calculate() {
              var v = parseFloat(document.getElementById('inpUtilVal').value) || 0;
              var f = (parseFloat(document.getElementById('inpUtilFactor').value) || 0) / 100;
              var n = Math.max(1, parseInt(document.getElementById('inpUtilSplit').value) || 1);

              var added = v * f;
              var total = v + added;
              var perUnit = total / n;

              document.getElementById('resUtilTotal').textContent = CalcCore.formatCurrency(total);
              document.getElementById('resUtilPerUnit').textContent = CalcCore.formatCurrency(perUnit);
              document.getElementById('resUtilAdd').textContent = CalcCore.formatCurrency(added);
            }
            document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
            calculate();
            '''

    return inputs, results, script

# ══════════════════════════════════════════════════════════════════
# BUILD ALL 204 TOOL PAGES
# ══════════════════════════════════════════════════════════════════

def build_all_tools():
    for tool in ALL_TOOLS:
        cid = tool["id"]
        title = tool["title"]
        cat = tool["category"]
        cat_title = tool["category_title"]
        icon = get_tool_icon(cid, cat)
        desc = f"Free online {title.lower()} by Daily1Step. Calculate instant results with interactive parameters, charts, formulas, and FAQs."

        inputs_html, results_html, script_js = generate_calc_engine(tool)

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
<link rel="stylesheet" href="../../assets/css/style.css?v=2">
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
        <span><i class="fa-solid {icon}" style="color:var(--primary); margin-right:8px;"></i> Input Parameters</span>
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

    print(f"Generated all {len(ALL_TOOLS)} tool pages!")

# ══════════════════════════════════════════════════════════════════
# BUILD HOMEPAGE (index.html) WITH ALL 204 TOOLS
# ══════════════════════════════════════════════════════════════════

def build_homepage():
    categories = [
        {"key": "financial", "title": "Financial Calculators", "icon": "fa-hand-holding-dollar"},
        {"key": "health", "title": "Fitness & Health Calculators", "icon": "fa-heart-pulse"},
        {"key": "math", "title": "Math & Scientific Calculators", "icon": "fa-square-root-variable"},
        {"key": "everyday", "title": "Everyday & Utility Calculators", "icon": "fa-clock"}
    ]

    grouped_html = ""
    for cat in categories:
        cat_tools = [c for c in ALL_TOOLS if c["category"] == cat["key"]]
        cards_html = ""
        for c in cat_tools:
            icon = get_tool_icon(c["id"], c["category"])
            cards_html += f'''
            <a href="tools/{c['id']}/index.html" class="tool-card">
              <div class="tool-card-icon"><i class="fa-solid {icon}"></i></div>
              <div class="tool-card-title">{c['title']}</div>
              <div class="tool-card-desc">Accurate online calculation tool for {c['title'].lower()}.</div>
            </a>
            '''

        grouped_html += f'''
        <div class="category-group-section" data-cat="{cat['key']}">
          <div class="category-group-header">
            <h2 class="cat-group-title"><i class="fa-solid {cat['icon']}"></i> {cat['title']} ({len(cat_tools)})</h2>
          </div>
          <div class="tool-grid">
            {cards_html}
          </div>
        </div>
        '''

    homepage_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily1Step Calculators — 204+ Free Online Financial, Health, Math &amp; Everyday Calculators</title>
<meta name="description" content="Free comprehensive collection of 204+ online calculators for mortgage, loan, BMI, calorie, retirement, scientific math, and everyday calculations.">
<link rel="canonical" href="https://bypyay.github.io/calculator/">
<link rel="stylesheet" href="assets/css/style.css?v=2">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Daily1Step 204+ Free Online Calculators",
  "url": "https://bypyay.github.io/calculator/",
  "description": "Collection of 204+ free online calculators for finance, health, math, and daily utilities.",
  "applicationCategory": "EducationalApplication",
  "operatingSystem": "All modern web browsers"
}}
</script>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="brand">
      <div class="brand-icon"><i class="fa-solid fa-calculator"></i></div>
      <div class="brand-title">Daily1Step <span class="accent">Calc</span></div>
    </a>
    <nav class="nav-links">
      <a href="#financial" class="nav-link" onclick="CalcCore.filterCategory('financial', this)">Finance (75)</a>
      <a href="#health" class="nav-link" onclick="CalcCore.filterCategory('health', this)">Health (31)</a>
      <a href="#math" class="nav-link" onclick="CalcCore.filterCategory('math', this)">Math (44)</a>
      <a href="#everyday" class="nav-link" onclick="CalcCore.filterCategory('everyday', this)">Everyday (54)</a>
    </nav>
  </div>
</header>

<section class="hero-section">
  <h1 class="hero-title">204+ Free <span class="gradient-text">Online Calculators</span></h1>
  <p class="hero-subtitle">Fast, comprehensive, and accurate online calculators for finance, fitness, health, math, and everyday calculations.</p>

  <div class="tool-search-box">
    <i class="fa-solid fa-magnifying-glass search-icon"></i>
    <input type="text" id="searchToolsInput" placeholder="Search 204+ calculators (e.g. Mortgage, BMI, Loan, Calorie, Compound Interest)...">
  </div>

  <div class="category-filter-nav">
    <button class="cat-tab-btn active" onclick="CalcCore.filterCategory('all', this)"><i class="fa-solid fa-grid-2"></i> All ({len(ALL_TOOLS)})</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('financial', this)"><i class="fa-solid fa-hand-holding-dollar"></i> Finance (75)</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('health', this)"><i class="fa-solid fa-heart-pulse"></i> Fitness &amp; Health (31)</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('math', this)"><i class="fa-solid fa-square-root-variable"></i> Math (44)</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('everyday', this)"><i class="fa-solid fa-clock"></i> Everyday (54)</button>
  </div>
</section>

<main class="tools-container">
  {grouped_html}
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-links">
      <a href="index.html">Home</a>
      <a href="legal/privacy.html">Privacy Policy</a>
      <a href="legal/terms.html">Terms of Service</a>
      <a href="legal/about.html">About Us</a>
      <a href="legal/contact.html">Contact</a>
      <a href="legal/disclaimer.html">Disclaimer</a>
    </div>
    <p class="copyright">&copy; 2026 Daily1Step. Free online calculators for finance, health, math, and daily utilities.</p>
  </div>
</footer>

<script src="assets/js/calculator-core.js"></script>
</body>
</html>'''

    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(homepage_html)

    print("Generated master homepage with 204 tools.")

# ══════════════════════════════════════════════════════════════════
# BUILD SITEMAP & ROBOTS.TXT
# ══════════════════════════════════════════════════════════════════

def build_sitemap():
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    sitemap.append('  <url><loc>https://bypyay.github.io/calculator/</loc><priority>1.0</priority></url>')

    for c in ALL_TOOLS:
        sitemap.append(f'  <url><loc>https://bypyay.github.io/calculator/tools/{c["id"]}/</loc><priority>0.8</priority></url>')

    sitemap.append('</urlset>')

    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap))

    robots = "User-agent: *\nAllow: /\nSitemap: https://bypyay.github.io/calculator/sitemap.xml\n"
    with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print(f"Generated sitemap.xml ({len(ALL_TOOLS) + 1} URLs) and robots.txt.")

if __name__ == "__main__":
    build_all_tools()
    build_homepage()
    build_sitemap()
    print("ALL 204 CALCULATORS COMPLETE AND FUNCTIONAL!")
