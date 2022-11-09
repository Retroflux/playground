mod print_to_console;
mod numbers;
mod variables;

fn main() {
    println!("Hello, world!");
    print_to_console::run();
    numbers::run();
    variables::run();
}
