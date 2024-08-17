// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

// Creating a contract
contract ConstructorExample {
    string public str;

    // Constructor function
    constructor() public {
        str = "GeeksForGeeks";
    }

    // Function to return the string value
    function getValue() public view returns (string memory) {
        return str;
    }
}
