mod print_to_console;
mod numbers;
mod variables;
mod types;
mod strings;

fn main() {
    println!("Hello, world!");
    print_to_console::run();
    numbers::run();
    variables::run();
    types::run();
    strings::run();
}
