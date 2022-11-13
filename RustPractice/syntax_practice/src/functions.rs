//Used to store blocks of code for re-use

pub fn run(){

   println!("\n\n\n Completing the same fizz buzz, but with functions for anything other than the conditional logic and looping structures:");
   for i in 1i8..100{
      if i % 15 == 0{
         print_fizz();
         print_buzz();
      }else if i % 5 == 0{
         print_buzz();
      }else if i % 3 == 0{
         print_fizz();
      }else{
         print_number(i);
      }
      print_single_whitespace();
   }

   // Strings are a little different as params compared to integers, so I'll specifaclly make note of that here
   greetings("Hello", "Jeremy");

   //Automatic returns exist in Rust
   for i in 1..10{
      let number1 = i;
      let number2 = 10-i;
      //function as part of declaration
      let ret_val : i32 = summate_numbers(number1, number2);
      println!("The summation of {number1} and {number2} is {ret_val}.");
   }

   //Closure example using the same code as previous; these are block scoped but can use outside variables
   let mut additional_weight = 10;
   for i in 1..10{
      let add_nums = |n1: i32, n2:i32, n3:i32| n1 + n2 + n3;
      additional_weight -= 1;
      println!("Closure summation: of {} + {} + {} = {}",i, 10-i, additional_weight, add_nums(i,10-i, additional_weight));
   }
}

//these are not public (pub omitted), so they are local to this functions file
fn print_fizz(){
   print!("fizz");
}

fn print_buzz(){
   print!("buzz");
}

fn print_number(number: i8){
   print!("{number}");
}

fn print_single_whitespace(){
   print!(" ");
}

fn greetings(greeting: &str, name: &str){
   println!("\n{} {}, it's nice to finally meet you IRL!", greeting, name);
}

//To automatically return something, don't use a semicolon on the line to return
fn summate_numbers(num1 : i32, num2: i32) -> i32{num1 + num2}