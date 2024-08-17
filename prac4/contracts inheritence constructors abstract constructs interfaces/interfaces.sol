// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Define the interface
interface Calculator {
    function getResult() external pure returns (uint);
}

// Implement the interface in a contract
contract SimpleCalculator is Calculator {
    function getResult() external pure override returns (uint) {
        uint a = 5;
        uint b = 10;
        return a + b;
    }
}
