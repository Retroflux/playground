
use std::vec;

pub fn run(){

   let mut numbers: Vec<i32> = vec![1, 2, 3, 4];

   println!("\n Vectors are resizable arrays");
   println!("These are the numbers in the vector: {:?}", numbers);

   //as long as you use the mut tag, you can increase the size of the vector
   numbers.push(69);
   numbers.push(420);

   for count  in  1..10{
      numbers.push(count);
   }
       
   for number in numbers.iter_mut(){
      *number *= 2;
   }

   //getting numbers is still the same process 
   println!("The vector is now {} wide and {} is the second value.\n{:?}", numbers.len(), numbers[1], numbers);

}