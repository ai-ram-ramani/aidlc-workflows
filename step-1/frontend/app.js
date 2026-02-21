/* Calculator App — Frontend Logic */

// UPDATE THIS after first CDK deployment with the API Gateway endpoint URL
const API_URL = "https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod";

// State
let operand1 = null;
let operator = null;
let waitingForOperand2 = false;

// DOM
const display = document.querySelector("[data-testid='calculator-display']");

function updateDisplay(value) {
    display.textContent = value;
    display.classList.remove("error");
}

function showError(message) {
    display.textContent = message;
    display.classList.add("error");
}

function handleDigit(digit) {
    if (waitingForOperand2) {
        updateDisplay(digit === "." ? "0." : digit);
        waitingForOperand2 = false;
        return;
    }

    const current = display.textContent;

    // Prevent multiple decimal points
    if (digit === "." && current.includes(".")) return;

    // Replace initial "0" unless adding decimal
    if (current === "0" && digit !== ".") {
        updateDisplay(digit);
    } else {
        updateDisplay(current + digit);
    }
}

function handleOperator(op) {
    const current = parseFloat(display.textContent);
    if (isNaN(current)) return;

    operand1 = current;
    operator = op;
    waitingForOperand2 = true;

    // Highlight active operator
    document.querySelectorAll(".btn-operator").forEach(function (btn) {
        btn.classList.remove("active");
    });
    var activeBtn = document.querySelector("[data-operator='" + op + "']");
    if (activeBtn) activeBtn.classList.add("active");
}

function handleClear() {
    operand1 = null;
    operator = null;
    waitingForOperand2 = false;
    updateDisplay("0");
    document.querySelectorAll(".btn-operator").forEach(function (btn) {
        btn.classList.remove("active");
    });
}

async function handleEquals() {
    if (operand1 === null || operator === null) return;

    var operand2 = parseFloat(display.textContent);
    if (isNaN(operand2)) return;

    // Clear operator highlight
    document.querySelectorAll(".btn-operator").forEach(function (btn) {
        btn.classList.remove("active");
    });

    try {
        var result = await sendCalculation(operand1, operand2, operator);
        updateDisplay(formatResult(result));
    } catch (err) {
        showError(err.message || "Calculation error");
    }

    // Reset state so next digit starts fresh
    operand1 = null;
    operator = null;
    waitingForOperand2 = false;
}

function formatResult(value) {
    // Avoid floating point display issues (e.g., 0.1 + 0.2 = 0.30000000000000004)
    var rounded = parseFloat(value.toFixed(10));
    return String(rounded);
}

async function sendCalculation(op1, op2, op) {
    var response = await fetch(API_URL + "/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ operand1: op1, operand2: op2, operator: op }),
    });

    var data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Server error");
    }

    return data.result;
}

// Event listeners
document.querySelectorAll(".btn-digit").forEach(function (btn) {
    btn.addEventListener("click", function () {
        handleDigit(btn.dataset.digit);
    });
});

document.querySelectorAll(".btn-operator").forEach(function (btn) {
    btn.addEventListener("click", function () {
        handleOperator(btn.dataset.operator);
    });
});

document.querySelector("[data-testid='btn-equals']").addEventListener("click", handleEquals);
document.querySelector("[data-testid='btn-clear']").addEventListener("click", handleClear);
