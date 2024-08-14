// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract OverloadingExample {
    function add(uint256 a, uint256 b) public pure returns (uint256) {
        return a + b;
    }
    function add(string memory a, string memory b) public pure returns (string memory)
    {
        return string(abi.encodePacked(a, b));
    }
}