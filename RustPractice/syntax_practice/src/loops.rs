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
   while count > 0 {

      print!("Count = {count}, fizzbuzz value = ");
      count-=1;
      if count % 15 == 0{
         println!("fizzbuzz ");
      }else if count % 3 == 0{
         println!("fizz ");
      }else if count % 5 == 0{
         println!("buzz ");
      }else{
         println!("{count} ");
      }

      if count >=101{
         break;
      }
   }


}