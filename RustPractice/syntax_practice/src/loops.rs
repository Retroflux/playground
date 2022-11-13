pub fn run(){
   let mut count = 0;

   //let's revamp the basic fizzbuzz code that we made in print_to_console.rs, but use a loop this time
   loop{

      count+=1;

      if count % 15 == 0{
         print!("fizzbuzz ");
      }else if count % 3 == 0{
         print!("fizz ");
      }else if count % 5 == 0{
         print!("buzz ");
      }else{
         print!("{count} ");
      }

      if count >=101{
         break;
      }
   }

   //reverse code as the infinite loop, but with a known exit value and printing one value per line beside the value of count 
   //commented out the print lines to avoid too much output
   while count > 0 {

      // print!("Count = {count}, fizzbuzz value = ");
      count -= 1;
      // if count % 15 == 0{
         // println!("fizzbuzz ");
      // }else if count % 3 == 0{
         // println!("fizz ");
      // }else if count % 5 == 0{
         // println!("buzz ");
      // }else{
         // println!("{count} ");
      // }
   }
   println!("\n\n");
   // Same as first batch of code, just counting to 20 with the for loop variable instead of count. Much more compact code!
   for i in 1..20{

      if i % 15 == 0{
         print!("fizzbuzz ");
      }else if i % 3 == 0{
         print!("fizz ");
      }else if i % 5 == 0{
         print!("buzz ");
      }else{
         print!("{i} ");
      }
   }

}