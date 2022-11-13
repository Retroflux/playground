mod print_to_console;
mod numbers;
mod variables;
mod types;
mod strings;
mod control_flow;
mod least_common_multiple;
mod tuples;
mod arrays;
mod vectors;
mod loops;

fn main() {
    println!("Hello, world!");
    print_to_console::run();
    numbers::run();
    variables::run();
    types::run();
    strings::run();
    control_flow::run();
    least_common_multiple::least_common_multiple_finder(4, 12);
    least_common_multiple::least_common_multiple_finder(5, 7);
    least_common_multiple::generalized_lcm_finder(&mut [2,2,5,10]);
    least_common_multiple::generalized_lcm_finder(&mut [10,15,3,10]);
    least_common_multiple::generalized_lcm_finder(&mut [2,7,5,10]);
    least_common_multiple::generalized_lcm_finder(&mut [2,2,4,4]);
    least_common_multiple::generalized_lcm_finder(&mut []);
    least_common_multiple::generalized_lcm_finder(&mut [2]);
    least_common_multiple::generalized_lcm_finder(&mut [2,3]);
    tuples::run();
    arrays::run();
    vectors::run();
    loops::run();
}
