pub fn run(){
   let mut count = 0;

   //let's revamp the basic fizzbuzz code that we made in print_to_console.rs, but use a loop this time
   loop{

      count+=1;

      if count % 3 == 0 && count % 5 == 0{
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
}