// use std::array;


pub fn least_common_multiple_finder(number1: i32, number2:i32){

    let stop_val = number1 * number2;
    let step_size: i32 = if number1 < number2 {number1} else {number2};
    let mut counter = step_size;

    while counter < stop_val {
        if counter % number1 == 0 && counter % number2 == 0{
           break;
        }
        counter += step_size;
    }

    

    println!("The lowest common multiple of {} and {} is {}", number1, number2, counter);
}

/*
When generalizing, it gets a little more complicated because you have to start working with
Option values that are produced the product. Luckily, since we know that there is always at least
two values in an LCM check, we can unwrap and dereference the Option to an i32 value.

after that, it's a matter of iterating through the array, checking if a stepping value mods
cleanly across all of the array values.
*/
pub fn generalized_lcm_finder(set_of_numbers: &mut [i32]){
    if set_of_numbers.len() == 0{
        println!("No numbers given! There is no LCM.");
        return;
    }else if set_of_numbers.len() == 1{
        println!("The lowest common multiple is {}",set_of_numbers[0]);
        return;
    }

    let stop_val: i32 = set_of_numbers.iter().product();
    let step_size: i32  = *(set_of_numbers.iter().min().unwrap());
    let mut counter = step_size;

    while counter < stop_val {
        let mut early_exit: bool = true;
        for i in 0..set_of_numbers.len(){
            if counter % set_of_numbers[i] != 0{
                early_exit = false;
                break;
            }
        }
        if early_exit{
            break;
        }
        counter += step_size;
    }

    println!("The lowest common multiple of {:?} is {}", set_of_numbers, counter);
}
