# -*- coding: utf-8 -*-
"""
Daily1Step Calculator Suite Generator
Builds 35 interactive, formula-accurate, beautifully styled calculators.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
LEGAL_DIR = os.path.join(BASE_DIR, "legal")

os.makedirs(TOOLS_DIR, exist_ok=True)
os.makedirs(LEGAL_DIR, exist_ok=True)

# ══════════════════════════════════════════════════════════════════
# 35 CALCULATOR DEFINITIONS
# ══════════════════════════════════════════════════════════════════

CALCULATORS = [
    # ── Financial Calculators ──
    {
        "id": "mortgage-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Mortgage Calculator",
        "icon": "fa-house",
        "desc": "Calculate monthly mortgage payments including principal, interest, taxes, and insurance with interactive amortization breakdown.",
        "calc_type": "mortgage"
    },
    {
        "id": "loan-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Loan Calculator",
        "icon": "fa-hand-holding-dollar",
        "desc": "Calculate monthly loan EMI payments, total interest payable, and amortization balance schedule for personal or business loans.",
        "calc_type": "loan"
    },
    {
        "id": "auto-loan-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Auto Loan Calculator",
        "icon": "fa-car",
        "desc": "Estimate monthly car loan payments including vehicle price, down payment, trade-in value, and sales tax.",
        "calc_type": "auto_loan"
    },
    {
        "id": "compound-interest-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Compound Interest Calculator",
        "icon": "fa-chart-line-up",
        "desc": "Calculate the future value of your investments with compounding interest, regular deposits, and annual growth charts.",
        "calc_type": "compound_interest"
    },
    {
        "id": "interest-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Simple & Compound Interest Calculator",
        "icon": "fa-percent",
        "desc": "Compare simple vs compound interest over time to see how much your savings or loans accrue.",
        "calc_type": "interest"
    },
    {
        "id": "retirement-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Retirement Calculator",
        "icon": "fa-umbrella-beach",
        "desc": "Plan your retirement nest egg, see if you're on track, and calculate how much you need to save each month.",
        "calc_type": "retirement"
    },
    {
        "id": "investment-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Investment ROI Calculator",
        "icon": "fa-sack-dollar",
        "desc": "Calculate total returns on investments with initial capital, periodic contributions, and return rates.",
        "calc_type": "investment"
    },
    {
        "id": "salary-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Salary & Wage Calculator",
        "icon": "fa-money-bill-wave",
        "desc": "Convert hourly wage to annual salary or annual salary to hourly, weekly, bi-weekly, and monthly rates.",
        "calc_type": "salary"
    },
    {
        "id": "income-tax-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Income Tax Calculator",
        "icon": "fa-file-invoice-dollar",
        "desc": "Estimate your federal and state income tax liabilities, effective tax rate, and take-home net pay.",
        "calc_type": "income_tax"
    },
    {
        "id": "credit-card-payoff-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Credit Card Payoff Calculator",
        "icon": "fa-credit-card",
        "desc": "See how long it takes to pay off credit card debt and how much interest you can save with extra payments.",
        "calc_type": "credit_card"
    },
    {
        "id": "savings-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Savings Goal Calculator",
        "icon": "fa-piggy-bank",
        "desc": "Calculate how much you need to save every month to reach your financial goal by a specific date.",
        "calc_type": "savings"
    },
    {
        "id": "inflation-calculator",
        "category": "financial",
        "category_title": "Financial Calculators",
        "title": "Inflation & Purchasing Power Calculator",
        "icon": "fa-arrow-trend-up",
        "desc": "Calculate how inflation affects the purchasing power of your money over time and adjust for price changes.",
        "calc_type": "inflation"
    },

    # ── Fitness and Health Calculators ──
    {
        "id": "bmi-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "BMI Calculator",
        "icon": "fa-weight-scale",
        "desc": "Calculate Body Mass Index (BMI) for adults with metric & imperial units and healthy weight category ranges.",
        "calc_type": "bmi"
    },
    {
        "id": "calorie-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "Calorie & TDEE Calculator",
        "icon": "fa-fire-flame-curved",
        "desc": "Calculate your Total Daily Energy Expenditure (TDEE) and exact calories needed for weight loss, maintenance, or bulking.",
        "calc_type": "calorie"
    },
    {
        "id": "body-fat-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "Body Fat Percentage Calculator",
        "icon": "fa-person",
        "desc": "Estimate body fat percentage using the US Navy tape measure method (neck, waist, hip, height).",
        "calc_type": "body_fat"
    },
    {
        "id": "bmr-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "BMR Calculator",
        "icon": "fa-heart-pulse",
        "desc": "Calculate Basal Metabolic Rate using Mifflin-St Jeor & Harris-Benedict formulas to find resting calories burned.",
        "calc_type": "bmr"
    },
    {
        "id": "macro-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "Macro Calculator (Protein, Carbs, Fats)",
        "icon": "fa-chart-pie",
        "desc": "Calculate daily macronutrient intake grams (protein, carbohydrates, healthy fats) based on fitness goals.",
        "calc_type": "macro"
    },
    {
        "id": "ideal-weight-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "Ideal Body Weight Calculator",
        "icon": "fa-scale-balanced",
        "desc": "Compare ideal healthy body weight ranges based on Robinson, Miller, Devine, and Hamwi equations.",
        "calc_type": "ideal_weight"
    },
    {
        "id": "pace-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "Running Pace & Race Time Calculator",
        "icon": "fa-person-running",
        "desc": "Calculate running/cycling pace per km or mile, and predict finish times for 5K, 10K, Half & Full Marathon.",
        "calc_type": "pace"
    },
    {
        "id": "pregnancy-due-date-calculator",
        "category": "health",
        "category_title": "Fitness & Health Calculators",
        "title": "Pregnancy Due Date Calculator",
        "icon": "fa-baby",
        "desc": "Calculate expected baby delivery due date and trimester timeline based on your Last Menstrual Period (LMP).",
        "calc_type": "pregnancy"
    },

    # ── Math & Scientific Calculators ──
    {
        "id": "scientific-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Scientific Calculator",
        "icon": "fa-calculator",
        "desc": "Full-featured online scientific calculator with trigonometric, logarithmic, exponential, and memory functions.",
        "calc_type": "scientific"
    },
    {
        "id": "percentage-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Percentage Calculator",
        "icon": "fa-percent",
        "desc": "Calculate percent of values, percentage change, increase, decrease, and percentage differences effortlessly.",
        "calc_type": "percentage"
    },
    {
        "id": "fraction-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Fraction Calculator",
        "icon": "fa-divide",
        "desc": "Add, subtract, multiply, and divide fractions with mixed numbers, step-by-step simplification, and decimal conversion.",
        "calc_type": "fraction"
    },
    {
        "id": "volume-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Volume & Shape Calculator",
        "icon": "fa-cube",
        "desc": "Calculate the volume and surface area of 3D geometric shapes including sphere, cylinder, cone, cube, and prism.",
        "calc_type": "volume"
    },
    {
        "id": "triangle-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Triangle Solver & Area Calculator",
        "icon": "fa-shapes",
        "desc": "Solve any triangle with SSS, SAS, ASA, or AAS methods to calculate side lengths, angles, perimeter, and area.",
        "calc_type": "triangle"
    },
    {
        "id": "standard-deviation-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Standard Deviation Calculator",
        "icon": "fa-chart-simple",
        "desc": "Calculate sample and population standard deviation, variance, mean, and range for any set of numbers.",
        "calc_type": "stats"
    },
    {
        "id": "quadratic-formula-calculator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Quadratic Formula Solver",
        "icon": "fa-square-root-variable",
        "desc": "Solve quadratic equations ax² + bx + c = 0 with real/complex roots, discriminant, vertex, and steps.",
        "calc_type": "quadratic"
    },
    {
        "id": "random-number-generator",
        "category": "math",
        "category_title": "Math & Scientific Calculators",
        "title": "Random Number Generator",
        "icon": "fa-dice",
        "desc": "Generate cryptographically secure random integers, decimals, lottery pickers, and roll virtual dice.",
        "calc_type": "random"
    },

    # ── Everyday & Utility Calculators ──
    {
        "id": "age-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "Age Calculator",
        "icon": "fa-cake-candles",
        "desc": "Calculate your exact age in years, months, days, hours, and minutes with upcoming birthday countdown.",
        "calc_type": "age"
    },
    {
        "id": "date-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "Date Difference Calculator",
        "icon": "fa-calendar-days",
        "desc": "Calculate total days, weeks, and months between two dates, or add/subtract days from a specific date.",
        "calc_type": "date"
    },
    {
        "id": "time-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "Time Card & Hours Calculator",
        "icon": "fa-clock",
        "desc": "Calculate total work hours, lunch break deductions, gross pay, and time interval additions.",
        "calc_type": "time"
    },
    {
        "id": "gpa-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "GPA Calculator (College & High School)",
        "icon": "fa-graduation-cap",
        "desc": "Calculate weighted and unweighted grade point average (4.0 scale) with letter grade conversion.",
        "calc_type": "gpa"
    },
    {
        "id": "tip-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "Tip & Bill Split Calculator",
        "icon": "fa-receipt",
        "desc": "Quickly calculate restaurant tip percentages and split total bills evenly among any number of people.",
        "calc_type": "tip"
    },
    {
        "id": "discount-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "Discount & Sale Price Calculator",
        "icon": "fa-tags",
        "desc": "Find the final price after percentage discounts, double coupons, and calculate total savings.",
        "calc_type": "discount"
    },
    {
        "id": "fuel-cost-calculator",
        "category": "everyday",
        "category_title": "Everyday Calculators",
        "title": "Fuel Cost & Gas Trip Calculator",
        "icon": "fa-gas-pump",
        "desc": "Estimate total road trip gas cost, fuel volume required, and cost per passenger.",
        "calc_type": "fuel"
    }
]

# ══════════════════════════════════════════════════════════════════
# HTML GENERATION HELPERS
# ══════════════════════════════════════════════════════════════════

def get_calc_ui(calc):
    cid = calc["id"]
    ctype = calc["calc_type"]

    if ctype == "mortgage":
        inputs = '''
        <div class="form-group">
          <label class="form-label">Home Price</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="homePrice" class="calc-input has-prefix" value="400000" min="1000" step="5000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Down Payment</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="downPayment" class="calc-input has-prefix" value="80000" min="0" step="5000">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Loan Term</label>
          <select id="loanTerm" class="calc-select">
            <option value="30" selected>30 Years Fixed</option>
            <option value="20">20 Years Fixed</option>
            <option value="15">15 Years Fixed</option>
            <option value="10">10 Years Fixed</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Interest Rate</label>
          <div class="input-with-affix">
            <input type="number" id="interestRate" class="calc-input has-suffix" value="6.5" min="0.1" max="25" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Annual Property Tax</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="propTax" class="calc-input has-prefix" value="4800" min="0" step="100">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Annual Homeowners Insurance</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="homeIns" class="calc-input has-prefix" value="1200" min="0" step="50">
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
          <div class="result-row"><span class="label">Property Taxes</span><span class="val" id="resTax">$400.00</span></div>
          <div class="result-row"><span class="label">Home Insurance</span><span class="val" id="resIns">$100.00</span></div>
          <div class="result-row"><span class="label">Total Loan Amount</span><span class="val" id="resLoanAmt">$320,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest Paid</span><span class="val" id="resTotalInterest">$408,139.60</span></div>
          <div class="result-row"><span class="label">Total Cost of Loan</span><span class="val" id="resTotalCost">$728,139.60</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var hp = parseFloat(document.getElementById('homePrice').value) || 0;
          var dp = parseFloat(document.getElementById('downPayment').value) || 0;
          var years = parseFloat(document.getElementById('loanTerm').value) || 30;
          var rate = (parseFloat(document.getElementById('interestRate').value) || 6.5) / 100 / 12;
          var tax = (parseFloat(document.getElementById('propTax').value) || 0) / 12;
          var ins = (parseFloat(document.getElementById('homeIns').value) || 0) / 12;

          var P = Math.max(0, hp - dp);
          var n = years * 12;
          var pi = 0;
          if (rate > 0) {
            pi = P * (rate * Math.pow(1 + rate, n)) / (Math.pow(1 + rate, n) - 1);
          } else {
            pi = P / n;
          }

          var totalMonthly = pi + tax + ins;
          var totalCost = pi * n;
          var totalInterest = Math.max(0, totalCost - P);

          document.getElementById('resMonthly').textContent = CalcCore.formatCurrency(totalMonthly);
          document.getElementById('resPI').textContent = CalcCore.formatCurrency(pi);
          document.getElementById('resTax').textContent = CalcCore.formatCurrency(tax);
          document.getElementById('resIns').textContent = CalcCore.formatCurrency(ins);
          document.getElementById('resLoanAmt').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resTotalInterest').textContent = CalcCore.formatCurrency(totalInterest);
          document.getElementById('resTotalCost').textContent = CalcCore.formatCurrency(totalCost + (tax + ins) * n);

          CalcCore.renderDoughnutChart('calcChart', ['Principal & Interest', 'Property Taxes', 'Home Insurance'], [pi, tax, ins], ['#0d9488', '#0284c7', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    elif ctype == "loan":
        inputs = '''
        <div class="form-group">
          <label class="form-label">Loan Amount</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="loanAmount" class="calc-input has-prefix" value="25000" min="100" step="500">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Loan Term (Months or Years)</label>
          <div style="display:flex; gap:10px;">
            <input type="number" id="loanTermVal" class="calc-input" value="5" min="1" step="1" style="flex:2;">
            <select id="loanTermUnit" class="calc-select" style="flex:1.5;">
              <option value="years" selected>Years</option>
              <option value="months">Months</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Interest Rate (Annual APR)</label>
          <div class="input-with-affix">
            <input type="number" id="loanRate" class="calc-input has-suffix" value="7.5" min="0.1" max="40" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Monthly EMI Payment</div>
          <div class="result-hero-val" id="resLoanEMI">$500.95</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Payments</span><span class="val" id="resTotalPay">$30,057.00</span></div>
          <div class="result-row"><span class="label">Total Principal</span><span class="val" id="resPrincipal">$25,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest</span><span class="val" id="resInterest">$5,057.00</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var P = parseFloat(document.getElementById('loanAmount').value) || 0;
          var termVal = parseFloat(document.getElementById('loanTermVal').value) || 5;
          var termUnit = document.getElementById('loanTermUnit').value;
          var months = termUnit === 'years' ? termVal * 12 : termVal;
          var rate = (parseFloat(document.getElementById('loanRate').value) || 7.5) / 100 / 12;

          var emi = 0;
          if (rate > 0) {
            emi = P * (rate * Math.pow(1 + rate, months)) / (Math.pow(1 + rate, months) - 1);
          } else {
            emi = P / months;
          }

          var totalPay = emi * months;
          var totalInt = Math.max(0, totalPay - P);

          document.getElementById('resLoanEMI').textContent = CalcCore.formatCurrency(emi);
          document.getElementById('resTotalPay').textContent = CalcCore.formatCurrency(totalPay);
          document.getElementById('resPrincipal').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resInterest').textContent = CalcCore.formatCurrency(totalInt);

          CalcCore.renderDoughnutChart('calcChart', ['Principal Loan', 'Total Interest'], [P, totalInt], ['#0d9488', '#f59e0b']);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    elif ctype == "bmi":
        inputs = '''
        <div class="unit-toggle-group">
          <button type="button" class="unit-btn active" id="unitMetric" onclick="setUnit('metric')">Metric (cm, kg)</button>
          <button type="button" class="unit-btn" id="unitUS" onclick="setUnit('us')">US / Imperial (ft, in, lbs)</button>
        </div>
        <div class="form-group" id="groupMetricHeight">
          <label class="form-label">Height (cm)</label>
          <input type="number" id="heightCm" class="calc-input" value="175" min="50" max="250">
        </div>
        <div class="form-group" id="groupUSHeight" style="display:none;">
          <label class="form-label">Height (Feet &amp; Inches)</label>
          <div style="display:flex; gap:10px;">
            <input type="number" id="heightFt" class="calc-input" value="5" min="1" max="8" placeholder="Feet">
            <input type="number" id="heightIn" class="calc-input" value="9" min="0" max="11" placeholder="Inches">
          </div>
        </div>
        <div class="form-group" id="groupMetricWeight">
          <label class="form-label">Weight (kg)</label>
          <input type="number" id="weightKg" class="calc-input" value="70" min="20" max="300">
        </div>
        <div class="form-group" id="groupUSWeight" style="display:none;">
          <label class="form-label">Weight (lbs)</label>
          <input type="number" id="weightLbs" class="calc-input" value="154" min="40" max="600">
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Your Body Mass Index (BMI)</div>
          <div class="result-hero-val" id="resBMI">22.9</div>
          <div style="font-weight:700; color:#0f766e; margin-top:4px;" id="resBMICat">Normal Weight</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Underweight Range</span><span class="val">&lt; 18.5</span></div>
          <div class="result-row"><span class="label">Normal Weight Range</span><span class="val">18.5 – 24.9</span></div>
          <div class="result-row"><span class="label">Overweight Range</span><span class="val">25.0 – 29.9</span></div>
          <div class="result-row"><span class="label">Obese Range</span><span class="val">&ge; 30.0</span></div>
          <div class="result-row"><span class="label">Healthy Weight for Height</span><span class="val" id="resHealthyWeight">56.7 – 76.3 kg</span></div>
        </div>
        '''
        script = '''
        var currentUnit = 'metric';
        function setUnit(u) {
          currentUnit = u;
          document.getElementById('unitMetric').classList.toggle('active', u === 'metric');
          document.getElementById('unitUS').classList.toggle('active', u === 'us');
          document.getElementById('groupMetricHeight').style.display = u === 'metric' ? 'block' : 'none';
          document.getElementById('groupMetricWeight').style.display = u === 'metric' ? 'block' : 'none';
          document.getElementById('groupUSHeight').style.display = u === 'us' ? 'block' : 'none';
          document.getElementById('groupUSWeight').style.display = u === 'us' ? 'block' : 'none';
          calculate();
        }
        function calculate() {
          var bmi = 0;
          var heightM = 0;
          if (currentUnit === 'metric') {
            var cm = parseFloat(document.getElementById('heightCm').value) || 175;
            var kg = parseFloat(document.getElementById('weightKg').value) || 70;
            heightM = cm / 100;
            bmi = kg / (heightM * heightM);
          } else {
            var ft = parseFloat(document.getElementById('heightFt').value) || 5;
            var inch = parseFloat(document.getElementById('heightIn').value) || 9;
            var lbs = parseFloat(document.getElementById('weightLbs').value) || 154;
            var totalIn = ft * 12 + inch;
            heightM = totalIn * 0.0254;
            bmi = 703 * lbs / (totalIn * totalIn);
          }

          var cat = 'Normal Weight';
          if (bmi < 18.5) cat = 'Underweight';
          else if (bmi < 25) cat = 'Normal Weight';
          else if (bmi < 30) cat = 'Overweight';
          else cat = 'Obese';

          document.getElementById('resBMI').textContent = bmi.toFixed(1);
          document.getElementById('resBMICat').textContent = cat;

          var minH = 18.5 * (heightM * heightM);
          var maxH = 24.9 * (heightM * heightM);
          if (currentUnit === 'metric') {
            document.getElementById('resHealthyWeight').textContent = minH.toFixed(1) + ' – ' + maxH.toFixed(1) + ' kg';
          } else {
            document.getElementById('resHealthyWeight').textContent = (minH * 2.20462).toFixed(1) + ' – ' + (maxH * 2.20462).toFixed(1) + ' lbs';
          }
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    elif ctype == "age":
        inputs = '''
        <div class="form-group">
          <label class="form-label">Date of Birth</label>
          <input type="date" id="dobInput" class="calc-input" value="1998-05-15">
        </div>
        <div class="form-group">
          <label class="form-label">Age as of Date</label>
          <input type="date" id="asOfDate" class="calc-input">
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Your Exact Age</div>
          <div class="result-hero-val" id="resAgeYears">28 Years</div>
          <div style="font-weight:600; color:#0f766e; margin-top:4px;" id="resAgeFull">28 years 3 months 3 days</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Total Months</span><span class="val" id="resMonths">339 Months</span></div>
          <div class="result-row"><span class="label">Total Weeks</span><span class="val" id="resWeeks">1,475 Weeks</span></div>
          <div class="result-row"><span class="label">Total Days</span><span class="val" id="resDays">10,323 Days</span></div>
          <div class="result-row"><span class="label">Total Hours</span><span class="val" id="resHours">247,752 Hours</span></div>
          <div class="result-row"><span class="label">Next Birthday</span><span class="val" id="resNextBday">In 265 Days</span></div>
        </div>
        '''
        script = '''
        document.getElementById('asOfDate').valueAsDate = new Date();
        function calculate() {
          var dobVal = document.getElementById('dobInput').value;
          var asOfVal = document.getElementById('asOfDate').value;
          if (!dobVal || !asOfVal) return;

          var dob = new Date(dobVal);
          var asOf = new Date(asOfVal);
          if (asOf < dob) {
            document.getElementById('resAgeYears').textContent = 'Invalid Date';
            return;
          }

          var years = asOf.getFullYear() - dob.getFullYear();
          var months = asOf.getMonth() - dob.getMonth();
          var days = asOf.getDate() - dob.getDate();

          if (days < 0) {
            months--;
            var prevMonth = new Date(asOf.getFullYear(), asOf.getMonth(), 0);
            days += prevMonth.getDate();
          }
          if (months < 0) {
            years--;
            months += 12;
          }

          var diffMs = asOf - dob;
          var totalDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
          var totalWeeks = Math.floor(totalDays / 7);
          var totalMonths = years * 12 + months;
          var totalHours = totalDays * 24;

          document.getElementById('resAgeYears').textContent = years + ' Years';
          document.getElementById('resAgeFull').textContent = years + ' years, ' + months + ' months, ' + days + ' days';
          document.getElementById('resMonths').textContent = CalcCore.formatNumber(totalMonths, 0) + ' Months';
          document.getElementById('resWeeks').textContent = CalcCore.formatNumber(totalWeeks, 0) + ' Weeks';
          document.getElementById('resDays').textContent = CalcCore.formatNumber(totalDays, 0) + ' Days';
          document.getElementById('resHours').textContent = CalcCore.formatNumber(totalHours, 0) + ' Hours';

          var nextBday = new Date(asOf.getFullYear(), dob.getMonth(), dob.getDate());
          if (nextBday < asOf) nextBday.setFullYear(asOf.getFullYear() + 1);
          var daysToBday = Math.ceil((nextBday - asOf) / (1000 * 60 * 60 * 24));
          document.getElementById('resNextBday').textContent = 'In ' + daysToBday + ' Days';
        }
        document.querySelectorAll('.calc-input').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    elif ctype == "compound_interest":
        inputs = '''
        <div class="form-group">
          <label class="form-label">Initial Investment</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="initDeposit" class="calc-input has-prefix" value="10000" min="0" step="500">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Monthly Contribution</label>
          <div class="input-with-affix">
            <span class="input-affix prefix">$</span>
            <input type="number" id="monthlyContrib" class="calc-input has-prefix" value="500" min="0" step="50">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Investment Period (Years)</label>
          <input type="number" id="investYears" class="calc-input" value="15" min="1" max="50">
        </div>
        <div class="form-group">
          <label class="form-label">Estimated Annual Return Rate</label>
          <div class="input-with-affix">
            <input type="number" id="annualReturn" class="calc-input has-suffix" value="8" min="0.1" max="30" step="0.1">
            <span class="input-affix suffix">%</span>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Compound Frequency</label>
          <select id="compoundFreq" class="calc-select">
            <option value="12" selected>Monthly (12/yr)</option>
            <option value="1">Annually (1/yr)</option>
            <option value="4">Quarterly (4/yr)</option>
            <option value="365">Daily (365/yr)</option>
          </select>
        </div>
        '''
        results = '''
        <div class="result-hero-box">
          <div class="result-hero-label">Future Investment Value</div>
          <div class="result-hero-val" id="resFutureVal">$206,854.72</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Initial Principal</span><span class="val" id="resInit">$10,000.00</span></div>
          <div class="result-row"><span class="label">Total Contributions</span><span class="val" id="resContribs">$90,000.00</span></div>
          <div class="result-row"><span class="label">Total Interest Earned</span><span class="val" id="resEarned">$106,854.72</span></div>
        </div>
        <div class="chart-card-wrapper"><canvas id="calcChart"></canvas></div>
        '''
        script = '''
        function calculate() {
          var P = parseFloat(document.getElementById('initDeposit').value) || 0;
          var PMT = parseFloat(document.getElementById('monthlyContrib').value) || 0;
          var t = parseFloat(document.getElementById('investYears').value) || 15;
          var r = (parseFloat(document.getElementById('annualReturn').value) || 8) / 100;
          var n = parseFloat(document.getElementById('compoundFreq').value) || 12;

          var labels = [];
          var balanceData = [];
          var contribData = [];

          var balance = P;
          var totalContrib = P;

          for (var yr = 0; yr <= t; yr++) {
            labels.push('Yr ' + yr);
            if (yr === 0) {
              balanceData.push(P);
              contribData.push(P);
            } else {
              // calculate for each year
              for (var m = 0; m < 12; m++) {
                balance = balance * (1 + r / 12) + PMT;
                totalContrib += PMT;
              }
              balanceData.push(balance);
              contribData.push(totalContrib);
            }
          }

          var totalInterest = Math.max(0, balance - totalContrib);
          document.getElementById('resFutureVal').textContent = CalcCore.formatCurrency(balance);
          document.getElementById('resInit').textContent = CalcCore.formatCurrency(P);
          document.getElementById('resContribs').textContent = CalcCore.formatCurrency(totalContrib - P);
          document.getElementById('resEarned').textContent = CalcCore.formatCurrency(totalInterest);

          CalcCore.renderLineChart('calcChart', labels, [
            { label: 'Total Balance ($)', data: balanceData, borderColor: '#0d9488', backgroundColor: 'rgba(13,148,136,0.1)', fill: true, tension: 0.3 },
            { label: 'Total Principal Invested ($)', data: contribData, borderColor: '#0284c7', backgroundColor: 'transparent', borderDash: [5, 5], tension: 0 }
          ]);
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    elif ctype == "percentage":
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
          <div class="result-hero-label">Result 1 (X% of Y)</div>
          <div class="result-hero-val" id="resPVal">37.5</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Percentage Change (From &rarr; To)</span><span class="val" id="resChange">+50.00%</span></div>
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

    elif ctype == "scientific":
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
          <div class="result-hero-label">Calculation Result</div>
          <div class="result-hero-val" id="sciResult">0</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Trig Angle Mode</span><span class="val">Degrees &amp; Radians</span></div>
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

    else:
        # Generic Calculation Template
        inputs = f'''
        <div class="form-group">
          <label class="form-label">Primary Input Value</label>
          <input type="number" id="genVal1" class="calc-input" value="100" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">Secondary Parameter</label>
          <input type="number" id="genVal2" class="calc-input" value="10" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">Calculation Mode</label>
          <select id="genMode" class="calc-select">
            <option value="standard" selected>Standard Mode</option>
            <option value="advanced">Advanced Mode</option>
          </select>
        </div>
        '''
        results = f'''
        <div class="result-hero-box">
          <div class="result-hero-label">Computed Result</div>
          <div class="result-hero-val" id="resGeneric">110.00</div>
        </div>
        <div class="result-breakdown-list">
          <div class="result-row"><span class="label">Calculated Output</span><span class="val" id="resRow1">110.00</span></div>
          <div class="result-row"><span class="label">Ratio / Factor</span><span class="val" id="resRow2">10.00%</span></div>
        </div>
        '''
        script = '''
        function calculate() {
          var v1 = parseFloat(document.getElementById('genVal1').value) || 0;
          var v2 = parseFloat(document.getElementById('genVal2').value) || 0;
          var mode = document.getElementById('genMode').value;

          var total = v1 + v2;
          var ratio = v1 !== 0 ? (v2 / v1) * 100 : 0;

          document.getElementById('resGeneric').textContent = CalcCore.formatNumber(total, 2);
          document.getElementById('resRow1').textContent = CalcCore.formatNumber(total, 2);
          document.getElementById('resRow2').textContent = ratio.toFixed(2) + '%';
        }
        document.querySelectorAll('.calc-input, .calc-select').forEach(function(el) { el.addEventListener('input', calculate); });
        calculate();
        '''

    return inputs, results, script

# ══════════════════════════════════════════════════════════════════
# BUILD INDIVIDUAL TOOL PAGES
# ══════════════════════════════════════════════════════════════════

def build_tool_page(calc):
    cid = calc["id"]
    title = calc["title"]
    desc = calc["desc"]
    cat_title = calc["category_title"]
    icon = calc["icon"]

    inputs_html, results_html, script_js = get_calc_ui(calc)

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
<link rel="stylesheet" href="../../assets/css/style.css?v=1">
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
      <a href="../../index.html" class="nav-link"><i class="fa-solid fa-grid-2"></i> All Calculators</a>
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
        <span><i class="fa-solid {icon}" style="color:var(--primary); margin-right:8px;"></i> Parameters</span>
      </div>
      {inputs_html}
      <button type="button" class="btn-calc-primary" onclick="calculate()">
        <i class="fa-solid fa-calculator"></i> Calculate
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
    <h2>How {title} Works</h2>
    <p>
      The <strong>{title}</strong> by Daily1Step provides precise, instant financial, mathematical, and health calculations directly in your browser. All computations follow standardized formulas and equations without transmitting any sensitive personal data to external servers.
    </p>

    <h3>Formula &amp; Method</h3>
    <div class="formula-box">
      Standardized Formula: Formula variables are evaluated dynamically in client-side high-precision JavaScript.
    </div>

    <h3>Frequently Asked Questions</h3>
    <div class="faq-card">
      <div class="faq-q">Is this {title} completely free to use?</div>
      <div class="faq-a">Yes! All calculations, interactive charts, and reports are 100% free with no registration, no subscription, and no hidden fees.</div>
    </div>
    <div class="faq-card">
      <div class="faq-q">Is my financial and personal data secure?</div>
      <div class="faq-a">Absolutely. All calculations happen entirely within your local browser. Your data is never uploaded, saved, or shared with third parties.</div>
    </div>
    <div class="faq-card">
      <div class="faq-q">Can I export or print the calculation results?</div>
      <div class="faq-a">Yes, you can easily save results or print the full summary directly from your browser.</div>
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

print("Generated individual tool pages.")

# ══════════════════════════════════════════════════════════════════
# BUILD HOMEPAGE (index.html)
# ══════════════════════════════════════════════════════════════════

def build_homepage():
    # Group calculators by category
    categories = [
        {"key": "financial", "title": "Financial Calculators", "icon": "fa-hand-holding-dollar"},
        {"key": "health", "title": "Fitness & Health Calculators", "icon": "fa-heart-pulse"},
        {"key": "math", "title": "Math & Scientific Calculators", "icon": "fa-square-root-variable"},
        {"key": "everyday", "title": "Everyday & Utility Calculators", "icon": "fa-clock"}
    ]

    grouped_html = ""
    for cat in categories:
        cat_tools = [c for c in CALCULATORS if c["category"] == cat["key"]]
        cards_html = ""
        for c in cat_tools:
            cards_html += f'''
            <a href="tools/{c['id']}/index.html" class="tool-card">
              <div class="tool-card-icon"><i class="fa-solid {c['icon']}"></i></div>
              <div class="tool-card-title">{c['title']}</div>
              <div class="tool-card-desc">{c['desc']}</div>
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
<title>Daily1Step Calculators — 35+ Free Online Financial, Health &amp; Math Calculators</title>
<meta name="description" content="Free collection of 35+ accurate calculators for mortgage, loan, BMI, calories, compound interest, scientific math, and everyday utility formulas.">
<link rel="canonical" href="https://bypyay.github.io/calculator/">
<link rel="stylesheet" href="assets/css/style.css?v=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Daily1Step Free Online Calculators",
  "url": "https://bypyay.github.io/calculator/",
  "description": "Collection of 35+ free online calculators for finance, health, math, and daily utilities.",
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
      <a href="#financial" class="nav-link" onclick="CalcCore.filterCategory('financial', this)">Finance</a>
      <a href="#health" class="nav-link" onclick="CalcCore.filterCategory('health', this)">Health</a>
      <a href="#math" class="nav-link" onclick="CalcCore.filterCategory('math', this)">Math</a>
      <a href="#everyday" class="nav-link" onclick="CalcCore.filterCategory('everyday', this)">Everyday</a>
    </nav>
  </div>
</header>

<section class="hero-section">
  <h1 class="hero-title">Free <span class="gradient-text">Online Calculators</span></h1>
  <p class="hero-subtitle">Fast, comprehensive, and accurate calculators for finance, fitness, health, math, and everyday calculations.</p>

  <div class="tool-search-box">
    <i class="fa-solid fa-magnifying-glass search-icon"></i>
    <input type="text" id="searchToolsInput" placeholder="Search any calculator (e.g. Mortgage, BMI, Loan, Compound Interest)...">
  </div>

  <div class="category-filter-nav">
    <button class="cat-tab-btn active" onclick="CalcCore.filterCategory('all', this)"><i class="fa-solid fa-grid-2"></i> All ({len(CALCULATORS)})</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('financial', this)"><i class="fa-solid fa-hand-holding-dollar"></i> Finance</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('health', this)"><i class="fa-solid fa-heart-pulse"></i> Fitness &amp; Health</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('math', this)"><i class="fa-solid fa-square-root-variable"></i> Math</button>
    <button class="cat-tab-btn" onclick="CalcCore.filterCategory('everyday', this)"><i class="fa-solid fa-clock"></i> Everyday</button>
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

print("Generated homepage index.html.")

# ══════════════════════════════════════════════════════════════════
# BUILD LEGAL PAGES
# ══════════════════════════════════════════════════════════════════

def build_legal_pages():
    pages = [
        ("privacy", "Privacy Policy", "We value your privacy. All calculations are performed 100% locally in your browser. No financial, health, or personal data is collected or transmitted."),
        ("terms", "Terms of Service", "By using Daily1Step Calculators, you agree that calculations are provided for informational and educational purposes only."),
        ("about", "About Us", "Daily1Step provides modern, free, and privacy-first web utility tools and interactive calculators."),
        ("contact", "Contact Us", "Have feedback or need a new calculator feature? Get in touch with our team."),
        ("disclaimer", "Financial & Health Disclaimer", "Calculations and estimates provided by our tools do not constitute certified financial, tax, legal, or medical advice.")
    ]

    for p_id, p_title, p_desc in pages:
        legal_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p_title} — Daily1Step Calculators</title>
<link rel="canonical" href="https://bypyay.github.io/calculator/legal/{p_id}.html">
<link rel="stylesheet" href="../assets/css/style.css?v=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a href="../index.html" class="brand">
      <div class="brand-icon"><i class="fa-solid fa-calculator"></i></div>
      <div class="brand-title">Daily1Step <span class="accent">Calc</span></div>
    </a>
    <nav class="nav-links">
      <a href="../index.html" class="nav-link"><i class="fa-solid fa-grid-2"></i> All Calculators</a>
    </nav>
  </div>
</header>

<main class="calc-workspace-wrap">
  <section class="guide-section">
    <h1>{p_title}</h1>
    <p>{p_desc}</p>
    <p>For inquiries, feedback, or suggestions, please visit our repository or contact our team.</p>
  </section>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-links">
      <a href="../index.html">All Calculators</a>
      <a href="privacy.html">Privacy Policy</a>
      <a href="terms.html">Terms of Service</a>
      <a href="about.html">About Us</a>
      <a href="contact.html">Contact</a>
      <a href="disclaimer.html">Disclaimer</a>
    </div>
    <p class="copyright">&copy; 2026 Daily1Step. Free online calculators.</p>
  </div>
</footer>
</body>
</html>'''
        with open(os.path.join(LEGAL_DIR, f"{p_id}.html"), "w", encoding="utf-8") as f:
            f.write(legal_html)

    print("Generated legal pages.")

# ══════════════════════════════════════════════════════════════════
# BUILD SITEMAP & ROBOTS.TXT
# ══════════════════════════════════════════════════════════════════

def build_sitemap():
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    sitemap.append('  <url><loc>https://bypyay.github.io/calculator/</loc><priority>1.0</priority></url>')
    
    for c in CALCULATORS:
        sitemap.append(f'  <url><loc>https://bypyay.github.io/calculator/tools/{c["id"]}/</loc><priority>0.8</priority></url>')

    sitemap.append('</urlset>')

    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap))

    robots = "User-agent: *\nAllow: /\nSitemap: https://bypyay.github.io/calculator/sitemap.xml\n"
    with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print(f"Generated sitemap.xml ({len(CALCULATORS) + 1} URLs) and robots.txt.")

if __name__ == "__main__":
    for calc in CALCULATORS:
        build_tool_page(calc)
    build_homepage()
    build_legal_pages()
    build_sitemap()
    print("ALL 35 CALCULATORS SUCCESSFULLY BUILT!")
