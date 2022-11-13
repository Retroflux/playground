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