use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "../../data/seaDepth.txt";
    // Open the file in read-only mode (ignoring errors).
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    let mut depth_difference_puzzle_1 = 0;
    let mut depth_difference_puzzle_2 = 0;
    let mut depth = vec![];

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for (index, line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let line_to_num: i32 = line.parse().unwrap();
        depth.push(line_to_num);
    
        if index >= 1 {
            if depth[index]>depth[index-1] {
                depth_difference_puzzle_1 += 1;
             }
        }

        if index >= 3 {
            if depth[index]>depth[index-3] {
                depth_difference_puzzle_2 += 1;
             }
        }
    }

    println! ("Depth difference in puzzle 1 {}: ", depth_difference_puzzle_1);
    println! ("Depth difference in puzzle 2 {}: ", depth_difference_puzzle_2);
    
}