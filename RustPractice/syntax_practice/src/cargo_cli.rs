use std::env;

pub fn run(){
   let args: Vec<String> = env::args().collect();

   println!("Args length: {}, args = {:?}", args.len(), args);

}