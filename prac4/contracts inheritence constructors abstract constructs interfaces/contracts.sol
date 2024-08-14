// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

// Contracts

contract Contract_demo {
    string message = "Hello";
    function dispMsg() public view returns (string memory) {
        return message;
    }
}

// Inheritence

contract Parent {
    uint256 internal sum;
    function setValue() external {
        uint256 a = 10;
        uint256 b = 20;
        sum = a + b;
    }
}
    
contract child is Parent {
    function getValue() external view returns (uint256) {
        return sum;
    }
}
    
contract caller {
    child cc = new child();
    function testInheritance() public returns (uint256) {
        cc.setValue();
        return cc.getValue();
    }
    function show_value() public view returns (uint256) {
        return cc.getValue();
    }
}

// constructors

// Creating a contract
contract constructorExample {
    string str;
    constructor() public {
        str = "GeeksForGeeks";
    }
    function getValue() public view returns (string memory) {
        return str;
    }
}