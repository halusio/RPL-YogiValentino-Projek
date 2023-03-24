const Calculator = require('./helper/UT_Helper_YogiValentino');

const resultAdd = Calculator.add(2, 3);
const resultSubtract = Calculator.subtract(5, 2);
const resultMultiply = Calculator.multiply(2, 4);
const resultDivide = Calculator.divide(6, 2);
console.log(resultAdd, resultSubtract, resultMultiply, resultDivide);
