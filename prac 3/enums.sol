// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract enumdemo {
    enum week_days {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday
    }
    week_days week;
    week_days choice;
    week_days constant default_value = week_days.Sunday;
    
    function set_value() public {
        choice = week_days.Tuesday;
    }
    function get_choice() public view returns (week_days) {
        return choice;
    }
    function get_defaultvalue() public pure returns (week_days) {
        return default_value;
    }
}

// Warning: Function state mutability can be restricted to pure