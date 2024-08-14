// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Arrays {
    //Static Array
    uint[3] arr2=[10,20,30];
    function dispstaticarray() public view returns(uint[3] memory)
    {
        return arr2;
    }
    //Dynamic Array
    uint x=5;
    uint [] arr1;
    function arrayDemo() public
    {
        while(x>0)
        {
            arr1.push(x);
            x=x-1;
        }
    }
    function dispdynamicarray() public view returns(uint[] memory)
    {
        return arr1;
    }
}

//ignore error like brackets