// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract variable_demo {
    uint sum = 4; //state variable
    string s = "welcome";

    function add(uint x) public {
        uint256 y = 2; //local variable sum = sum+x+y:
        sum = sum + x + y;
        }
    function display() public view returns (uint256) {
        return sum;
    }
    function displayMsg() public view returns (string memory) {
        return s;
    }
}