// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Test{
    function CallAddMod() public pure returns(uint){
        return addmod(7,3,3);
    }
    function CallMulMod() public pure returns(uint){
        return mulmod(7,3,3);
    }
}