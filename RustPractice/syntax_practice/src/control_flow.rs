/*

control flow is predicated on true/false situations. if 0, false; else, true
    in Rust, this is limited to just bool values (0 or 1) - it will not interpolate ints
    the below comments code will not work

        let number = 3;

        if number {
            println!("The number {} resolves to true, even though it's not 0 or 1", number);
        }


*/

pub fn run(){

    // if you want to check an integer in a bool-like setting (required for conditional branching),
    // you would have to do this:

    let number = 3;
    
    if number != 0{
        println!("The number {} resolves to true, even though it's not 0 or 1, because we're completing a comparison that resolves to a bool", number);

    }

    // You can also assign values based on conditions

    let condition_value: i32 = 23;

    let uncertain_value: i32 = if condition_value % 2 == 1 {1} else {0};

    println!("Uncertain Value = {uncertain_value}, which is the remainder of condition_value mod 2");

    //chaining conditional statements

    if number > 4{
        println!("This is a group of people");
    } else if number < 2{
        println!("This can't even be a group, there's not enough people!");
    } else if number == 2 {
        println!("This number is a couple, not a group!");
    } else{
        println!("This is most certainly the correct number of people");
    }



}
