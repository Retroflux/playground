/*There are two types of strings:

str = primitive string, fixed in length, immutable
String = growable, heap-allocated data structure; used when you need to modify or own data

String functions: https://doc.rust-lang.org/std/string/struct.String.html

*/

pub fn run(){

   println!("Strings begin:");

   let mut growable_string = String::from("Hello");

   //Get length

   println!("length of growable_string: {}", growable_string.len());


   // Push only char variables
   growable_string.push('!');

   println!("{}", growable_string);

   //Push string of characters
   growable_string.push_str(" You stinky guy");

   println!("{}", growable_string);
   println!("length of growable_string: {}", growable_string.len());

   let is_the_string_empty = growable_string.is_empty();

   println!("String is empty: {:?}", is_the_string_empty);

   //Loop through strings  
   for word in growable_string.split_whitespace(){
      println!("{}\n",word);
   }

}

