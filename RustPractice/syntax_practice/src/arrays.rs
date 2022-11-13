// arrays are a fixed size, where all of the elements are the same datatype, unlike vectors

pub fn run(){

   println!("Arrays and stuff: \n\n");

   //can also be mutable, 
   let numbers : [i32; 5] = [1,2,3,4,5];

   println!("Can be printed with the debug trait: {:?}", numbers);

   print!("\n...or, you can print it with a for loop: ");
   for item in numbers{
      print!("{} ",item);
   }

   //Can also print single values from the array with standard indexing values
   println!("\nThe second value in the array is: {}", numbers[1]);


   //standard built-in functions are also included
   println!("This length of the array ({}) cannot be changed!!!\n", numbers.len());

   //this is just a cool thing I found while researching: you can grab the size of it because it's stack-allocated
   println!("The array occupies {} bytes.", std::mem::size_of_val(&numbers));

   //slices are similar to Python, but more explicit on the bounds
   let slice: &[i32] = &numbers[1..3];
   println!("A two-wide slice across [1..3] is {:?}; only two-wide, with the right-bound being omitted. Technically it should be [1..3), but I digress.", slice);

}
