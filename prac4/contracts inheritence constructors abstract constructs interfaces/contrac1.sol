// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Contract_demo {
    string message = "Hello";
    
    function dispMsg() public view returns (string memory) {
        return message;
    }
}
