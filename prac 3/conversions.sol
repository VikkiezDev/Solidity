// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract ImplicitConversion {
    function add() public pure returns (uint256) 
    {
        uint256 a = 10;
        uint256 b = 20;
        return a + b;
    }
}

contract ExplicitConversion {
    function convert() public pure returns (bytes memory) 
    {
        string memory str = "Hello World";
        bytes memory b = bytes(str);
        return b;
    }
}