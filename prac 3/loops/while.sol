// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract whiledemo
{
    uint [] data;
    uint x=0;

    function whileLoopDemo() public
    {
        while(x<5)
        {
            data.push(x);
            x=x+1;
        }
    }

    function dispwhileloop() public view returns(uint[] memory)
    {
        return data;
    }
}