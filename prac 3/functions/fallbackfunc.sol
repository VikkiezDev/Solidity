// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract A {
    uint256 n;
    function set(uint256 value) external {
        n = value;
    }
    receive() external payable {
        n = 0;
    }
}

contract example {
    function callA(A a) public returns (bool) {
        (bool success, ) = address(a).call(abi.encodeWithSignature("setter()"));
        require(success);
        address payable payableA = payable(address(uint160(uint160(address(a)))));
        return (payableA.send(2 ether));
    }
}