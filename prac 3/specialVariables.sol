// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Special_Variables {
    mapping(address => uint256) rollNo;
    function setRollNO(uint256 _myNumber) public {
        rollNo[msg.sender] = _myNumber;
    }
    function whatIsMyRollNumber() public view returns (uint256) {
        return rollNo[msg.sender];
    }
}