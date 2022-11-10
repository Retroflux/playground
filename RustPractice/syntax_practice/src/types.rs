/*
Primitive Types--
Integers: u8, i8, u16, i16, u32, i32, u64, i64, u128, i128 (number of bits they take in memory)
Floats: f32, f64
Boolean (bool)
Characters (char)
Tuples
Arrays
*/

/* 
- Arrays are fixed types, vectors are growable arrays 
- Rust is statically typed, but can infer when it is compiled based on how we use it
*/

pub fn run(){

   //defaults to i32
   let x = 1;

   //defaults to f64
   let x2 = 1.23456; 

   //forcing the type

   let x3: i8 =  127;

   //find max
   let x4: i32 = std::i32::MAX;
   let x5: i64 = std::i64::MAX;

   //Find max


   println!("\n x: {} x2: {} x3: {} x4: {}, x5: {}", x, x2, x3, x4, x5);


   //Boolean

   let is_active = true;
   let is_inactive:bool = !(is_active);

   let math_works:bool = 10.0 > 8.333; //is there a better way to do this?


   println!("Is it active: {:?}\nIs it inactive: {:?}\nMath in expressions: {:?}\n",is_active, is_inactive, math_works);

   //char variables

   let unicode_char = '\u{1F600}';

   println!("{0}{0}{0}{0}{0}{0}{0}{0}{0} \n\n", unicode_char);



}