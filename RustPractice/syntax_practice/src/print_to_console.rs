pub fn run(){
    //Print to console
    println!("Hello from the print_to_console.rs file!");

    //Placeholder arguments
    println!("format {} arguments", "some");
    println!("The world is {} and humanity is {}", "big", "small");
    println!("1, 2, {0}, 4, {1}, {0}, 7, 8, {0}, {1}, 11, {0}, 13, 14, {0}{1}", "fizz", "buzz");
    println!("{character1} likes apples but {character2} hates them", character1="Bobby", character2 = "Rajesh" );

    //Fancy stuff
    print!("This line will print without a newline so");
    println!("I can finish it on this line!");

    println!("Numbers with different bases; Binary for 10 {:b}, Hexadecimal for 10
    {:x}, Octal for 10 {:o}", 10, 10, 10);
    println!("A println can be used to insert an empty line, or the slash-n can be used at the end of an output line. \n\n");

}