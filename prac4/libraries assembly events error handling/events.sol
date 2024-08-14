// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract eventExample {
    // Declaring state variables
    uint256 public value = 0;
    // Declaring an event
    event Increment(address owner);
    // Defining a function for logging event
    function getValue(uint256 _a, uint256 _b) public {
        emit Increment(msg.sender);
        value = _a + _b;
    }
}