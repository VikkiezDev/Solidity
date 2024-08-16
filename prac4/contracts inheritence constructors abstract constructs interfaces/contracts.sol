//1]contract

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Contract_demo {
    string message = "Hello";
    
    function dispMsg() public view returns (string memory) {
        return message;
    }
}


//2]inheritence
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

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


//3]constructor
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
