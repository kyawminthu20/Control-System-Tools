# 🦀 Rust Mastery Roadmap: Zero to Professional

## Your Starting Point Assessment
```
✅ Basic C knowledge   → You understand pointers, memory (helpful!)
✅ Basic Python knowledge → You understand logic, loops, functions
❌ Zero Rust knowledge  → We start from absolute scratch
```

---

## PHASE 0: Pre-Rust Foundations (1–2 Weeks)
> *Strengthen prerequisites so Rust concepts click faster*

### What to Brush Up On
```
□ How memory works (stack vs heap)
□ What pointers and references are (from C)
□ Basic data structures (arrays, linked lists, hash maps)
□ Command line / terminal comfort
□ Basic Git (clone, commit, push, branch)
```

### Action Items
| Task | Resource |
|------|----------|
| Memory fundamentals | CS50 (YouTube, first 3 lectures) |
| Git basics | "Git It" interactive tutorial |
| Terminal comfort | Practice navigating, creating files via CLI |

---

## PHASE 1: Rust Fundamentals (Weeks 1–4)
> *Goal: Write simple programs, understand what makes Rust unique*

### Week 1 — Setup & Absolute Basics
```
□ Install Rust via rustup (https://rustup.rs)
□ Understand cargo (Rust's build tool & package manager)
□ cargo new, cargo build, cargo run, cargo check
□ Hello World
□ Variables & mutability (let vs let mut)
□ Basic data types (i32, f64, bool, char, &str, String)
□ Functions and return values
□ Comments
```

#### Practice Project
```rust
// Build a temperature converter (Celsius <-> Fahrenheit)
fn celsius_to_fahrenheit(c: f64) -> f64 {
    c * 9.0 / 5.0 + 32.0
}
```

### Week 2 — Control Flow & Core Concepts
```
□ if / else if / else
□ loop, while, for
□ Ranges (1..10, 1..=10)
□ Tuples and arrays
□ String vs &str (start understanding)
□ User input (std::io)
□ Basic error handling with .expect()
```

#### Practice Project
```
→ Number guessing game (from The Rust Book Chapter 2)
→ FizzBuzz
→ Simple calculator (read input, parse, compute)
```

### Week 3 — Ownership (THE Critical Concept)
```
□ ⭐ Ownership rules (3 rules — memorize them)
□ ⭐ Borrowing (&T and &mut T)
□ ⭐ Lifetimes (basic understanding)
□ The borrow checker — learn to READ error messages
□ Move semantics
□ Clone vs Copy
□ Stack vs Heap in Rust context
```

> **⚠️ THIS IS THE HARDEST PART OF RUST. Spend extra time here.**

```rust
// Understand WHY this fails:
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;        // s1 is MOVED
    // println!("{s1}"); // ❌ ERROR: s1 no longer valid
    println!("{s2}");    // ✅ works
}
```

#### Practice
```
→ Rewrite previous projects being mindful of ownership
→ Intentionally trigger borrow checker errors & fix them
→ Do Rustlings exercises (ownership section)
```

### Week 4 — Structs, Enums & Pattern Matching
```
□ Structs (named fields, tuple structs, unit structs)
□ impl blocks and methods
□ Enums (with data variants)
□ Option<T> (Rust's null replacement)
□ Result<T, E> (Rust's error handling)
□ match expressions (exhaustive pattern matching)
□ if let / while let
```

#### Practice Project
```
→ Build a contact book (struct for Contact, Vec to store)
→ Build a basic enum-based state machine
```

### 📚 Phase 1 Resources
| Resource | Type | Priority |
|----------|------|----------|
| **"The Rust Programming Language" Book** (a.k.a. "The Book") Ch 1–6 | Reading | 🔴 Essential |
| **Rustlings** (github.com/rust-lang/rustlings) | Exercises | 🔴 Essential |
| **Rust By Example** (doc.rust-lang.org/rust-by-example) | Reference | 🟡 Recommended |
| **Let's Get Rusty** (YouTube) | Video | 🟡 Recommended |

---

## PHASE 2: Intermediate Rust (Weeks 5–10)

### Week 5–6 — Collections, Error Handling & Modules
```
□ Vec<T>, HashMap<K,V>, HashSet<T>
□ Iterators (.iter(), .map(), .filter(), .collect())
□ Iterator chaining
□ Proper error handling (Result, ?, custom errors)
□ Modules & project structure (mod, pub, use)
□ Crates and Cargo.toml dependencies
□ Reading documentation (docs.rs)
```

#### Practice Project
```
→ Word frequency counter (read file, count words, sort)
→ CSV parser (read, process, output)
```

### Week 7–8 — Traits, Generics & Lifetimes
```
□ Traits (Rust's version of interfaces)
□ Implementing standard traits (Display, Debug, Clone, PartialEq)
□ Generics (<T>) in functions, structs, enums
□ Trait bounds (T: Display + Clone)
□ Lifetimes ('a) — deep understanding
□ Where clauses
□ Trait objects (dyn Trait) vs static dispatch
□ Deriving traits (#[derive(...)])
```

```rust
// Example: Generic function with trait bounds
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}
```

#### Practice Project
```
→ Build a generic data structure (e.g., a simple stack)
→ Build a plugin-like system using traits
```

### Week 9–10 — Closures, Smart Pointers & Advanced Types
```
□ Closures (|x| x + 1) and Fn, FnMut, FnOnce
□ Box<T> (heap allocation)
□ Rc<T> (reference counting)
□ RefCell<T> (interior mutability)
□ Arc<T> (atomic reference counting)
□ Type aliases
□ Newtype pattern
□ The Deref and Drop traits
```

#### Practice Project
```
→ Build a simple linked list using Box<T>
→ Build a tree structure
→ Mini in-memory database with HashMap + custom types
```

### 📚 Phase 2 Resources
| Resource | Type | Priority |
|----------|------|----------|
| **The Rust Book** Ch 7–15 | Reading | 🔴 Essential |
| **Exercism Rust Track** | Exercises | 🔴 Essential |
| **Rust By Practice** (practice.rs) | Exercises | 🟡 Recommended |
| **"Programming Rust" (O'Reilly, 2nd ed)** | Book | 🟡 Recommended |

---

## PHASE 3: Applied Rust (Weeks 11–18)

### Week 11–12 — Concurrency & Async
```
□ Threads (std::thread::spawn)
□ Message passing (channels: mpsc)
□ Shared state (Mutex<T>, Arc<Mutex<T>>)
□ Send and Sync traits
□ async/await basics
□ Tokio runtime (the standard async runtime)
□ Futures
□ Async file I/O and networking
```

#### Practice Project
```
→ Multi-threaded web scraper
→ Concurrent file processor
→ Simple chat server using Tokio
```

### Week 13–14 — CLI & File I/O & Testing
```
□ Building CLI tools (clap crate)
□ File I/O (std::fs, BufReader, BufWriter)
□ Serialization (serde, serde_json, serde_yaml)
□ Unit tests (#[test], assert!, assert_eq!)
□ Integration tests (/tests directory)
□ Documentation tests
□ Benchmarking basics
□ Error crates (thiserror, anyhow)
```

#### Practice Project
```
→ CLI todo app (add, list, complete, delete tasks — saved to JSON)
→ Log file analyzer
→ Config file parser
```

### Week 15–16 — Web Development in Rust
```
□ HTTP basics review
□ Actix-web OR Axum framework
□ REST API design
□ Routing, handlers, middleware
□ Database (SQLx or Diesel with PostgreSQL/SQLite)
□ Authentication basics
□ Request validation
```

#### Practice Project
```
→ REST API for a bookstore/blog
→ URL shortener service
→ Simple CRUD app with database
```

### Week 17–18 — Systems Programming Concepts
```
□ Unsafe Rust (raw pointers, unsafe blocks — when & why)
□ FFI (calling C from Rust, calling Rust from C)
□ Basic macro_rules! macros
□ Procedural macros (awareness level)
□ Memory layout and repr
□ Working with OS APIs
□ Basic networking (std::net)
```

#### Practice Project
```
→ Wrap a C library using FFI
→ Build a simple HTTP server from scratch (std::net only)
→ Write a custom derive macro
```

### 📚 Phase 3 Resources
| Resource | Type | Priority |
|----------|------|----------|
| **The Rust Book** Ch 16–20 | Reading | 🔴 Essential |
| **Tokio Tutorial** (tokio.rs/tokio/tutorial) | Tutorial | 🔴 Essential |
| **Zero To Production In Rust** (Luca Palmieri) | Book | 🔴 Essential |
| **Rust Atomics and Locks** (Mara Bos) | Book | 🟡 For concurrency depth |
| **Axum docs + examples** | Reference | 🟡 Recommended |

---

## PHASE 4: Advanced Rust (Weeks 19–26)

### Topics to Master
```
□ Advanced lifetimes (HRTB: for<'a>)
□ Advanced trait patterns (associated types, GATs)
□ Advanced generics (PhantomData, turbofish ::<>)
□ Pin and Unpin (for async)
□ Cow<T> (clone on write)
□ Advanced error handling patterns
□ Performance profiling (flamegraph, criterion)
□ SIMD basics
□ no_std programming (embedded awareness)
□ Compiler plugins and build scripts (build.rs)
□ Workspace management (multi-crate projects)
□ Publishing crates to crates.io
□ CI/CD for Rust (GitHub Actions)
□ Clippy lints and rustfmt configuration
```

### Deep Dive: Choose a Specialization Track

```
┌─────────────────────────────────────────────────┐
│         PICK 1-2 SPECIALIZATIONS                │
├─────────────────────────────────────────────────┤
│                                                 │
│  🌐 Backend/Web     → Axum, SQLx, gRPC (tonic) │
│  🖥️  Systems         → OS, networking, embedded  │
│  🎮 Game Dev        → Bevy engine               │
│  ⛓️  Blockchain/Web3 → Solana, Substrate         │
│  📊 Data/ML         → Polars, ndarray            │
│  🔧 DevTools        → CLI tools, compilers       │
│  🌍 WebAssembly     → wasm-bindgen, Yew, Leptos │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 📚 Phase 4 Resources
| Resource | Type | Priority |
|----------|------|----------|
| **"Rust for Rustaceans" (Jon Gjengset)** | Book | 🔴 Essential |
| **Jon Gjengset YouTube (Crust of Rust series)** | Video | 🔴 Essential |
| **"Rust Atomics and Locks"** | Book | 🟡 Recommended |
| **Rust RFC repository** | Reading | 🟢 Optional |
| **This Week in Rust newsletter** | Newsletter | 🟡 Recommended |

---

## PHASE 5: Professional Level (Weeks 27–52+)
> *Go from "I know Rust" to "I'm a professional Rust developer"*

### Portfolio Projects (Build 3–5 Major Projects)

```
PROJECT 1 (Systems): 
  → Build a Redis clone or simple database engine

PROJECT 2 (Web):
  → Full-stack app with Rust backend + auth + DB + deployment

PROJECT 3 (Tool):
  → A developer tool others can use (publish to crates.io)

PROJECT 4 (Your specialization):
  → Domain-specific project showing depth

PROJECT 5 (Open Source Contribution):
  → Contribute to a real Rust project
```

### Professional Skills
```
□ Read and understand any Rust codebase
□ Write idiomatic Rust (not "C in Rust" or "Python in Rust")
□ Design APIs that leverage Rust's type system
□ Performance optimization
□ Unsafe code auditing
□ Code review ability
□ Write comprehensive tests
□ Document your code properly
□ Mentor others in Rust
```

### Open Source Contributions
```
Start here:
  → Look for "good first issue" labels on GitHub
  → Contribute to: Tokio, Serde, Axum, Bevy, or Clippy
  → Fix documentation (easy entry point!)
  → Publish your own crate
```

### Career Actions
```
□ Build a GitHub portfolio with pinned Rust projects
□ Write blog posts about Rust concepts you've learned
□ Answer Rust questions on StackOverflow/Reddit
□ Join Rust Discord and help others
□ Attend Rust meetups or RustConf
□ Get Rust-related certifications (if available)
□ Apply for Rust positions / freelance projects
```

---

## 📅 Daily Study Plan Template

```
╔══════════════════════════════════════════╗
║         DAILY ROUTINE (1.5-3 hrs)        ║
╠══════════════════════════════════════════╣
║                                          ║
║  📖 30 min — Read (The Book / resource)  ║
║  💻 60 min — Code (exercises/projects)   ║
║  🔍 15 min — Read Rust source/docs       ║
║  📝 15 min — Review & journal learnings  ║
║                                          ║
║  WEEKLY:                                 ║
║  🏗️  Weekend — Work on project (2-4 hrs) ║
║  👥 1x — Engage with Rust community      ║
║                                          ║
╚══════════════════════════════════════════╝
```

---

## 🧰 Complete Tool & Resource Summary

### Must-Have Tools
```
rustup          — Toolchain manager
cargo           — Build system & package manager
rust-analyzer   — IDE support (VS Code extension)
clippy          — Linter (cargo clippy)
rustfmt         — Formatter (cargo fmt)
VS Code         — Recommended editor for beginners
```

### Book Priority Order
```
1. "The Rust Programming Language" (free online)     ← START HERE
2. "Zero to Production in Rust" (web focus)
3. "Programming Rust, 2nd Edition" (deep reference)
4. "Rust for Rustaceans" (advanced)
5. "Rust Atomics and Locks" (concurrency)
```

### Practice Platforms
```
1. Rustlings          → Beginner exercises
2. Exercism Rust Track → Graded exercises with mentoring
3. practice.rs        → Bite-sized practice
4. Advent of Code     → Algorithm challenges
5. LeetCode (in Rust) → Interview prep
6. Codewars           → Kata challenges
```

### Community
```
→ r/rust (Reddit)
→ Rust Discord (official)
→ Rust Users Forum (users.rust-lang.org)
→ This Week in Rust (newsletter)
→ Rust YouTube: Let's Get Rusty, Jon Gjengset, 
                 No Boilerplate, fasterthanlime
```

---

## 🎯 Milestones Checklist

```
Phase 0  □ Environment ready, Git comfortable
Phase 1  □ Can write basic programs, understand ownership
Phase 2  □ Can use generics/traits, build multi-file projects  
Phase 3  □ Can build web APIs, CLI tools, use async
Phase 4  □ Can read any Rust code, write idiomatic Rust
Phase 5  □ Portfolio ready, contributing to open source
         □ Can design and architect Rust applications
         □ PROFESSIONAL RUST DEVELOPER ✅
```

---

## ⚡ Key Mindset Tips

> 1. **The compiler is your teacher** — Read error messages carefully; Rust has the BEST error messages of any language
> 2. **Fight the borrow checker early, befriend it later** — It feels restrictive at first, then becomes your superpower
> 3. **Don't skip ownership** — It's the foundation of EVERYTHING in Rust
> 4. **Write ugly code first, then make it idiomatic** — Don't chase perfection early
> 5. **Build things YOU care about** — Motivation matters more than curriculum
> 6. **It's normal to feel slow** — Rust has a steep learning curve but a high ceiling

**Estimated timeline: 9–12 months to professional level with consistent daily practice (1.5–3 hours/day).**

Start today: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` 🦀

# 🦀 Rust Basics — Complete Beginner Guide

## 1. Setup & First Program

### Install Rust
```bash
# Install rustup (Rust toolchain manager)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verify installation
rustc --version
cargo --version
```

### Create Your First Project
```bash
cargo new hello_rust    # Create new project
cd hello_rust           # Enter project directory
cargo run               # Build and run
```

### Project Structure
```
hello_rust/
├── Cargo.toml          # Project config (like package.json)
└── src/
    └── main.rs         # Your main code file
```

### Hello World
```rust
fn main() {
    println!("Hello, World!");    // println! is a macro (note the !)
}
```

### Cargo Commands
```bash
cargo new project_name   # Create new project
cargo build              # Compile the project
cargo run                # Compile and run
cargo check              # Check for errors (fast, no binary)
cargo clean              # Remove build artifacts
```

---

## 2. Variables & Mutability

```rust
fn main() {
    // ========== IMMUTABLE BY DEFAULT ==========
    let x = 5;
    // x = 10;          // ❌ ERROR! Variables are immutable by default
    println!("x = {}", x);

    // ========== MUTABLE VARIABLES ==========
    let mut y = 5;       // `mut` makes it mutable
    println!("y = {}", y);
    y = 10;              // ✅ This works now
    println!("y = {}", y);

    // ========== CONSTANTS ==========
    const MAX_POINTS: u32 = 100_000;   // Must have type, SCREAMING_SNAKE_CASE
    println!("Max: {}", MAX_POINTS);

    // ========== SHADOWING ==========
    let z = 5;
    let z = z + 1;      // ✅ This creates a NEW variable (shadowing)
    let z = z * 2;
    println!("z = {}", z);  // z = 12

    // Shadowing can even change types!
    let spaces = "   ";         // &str type
    let spaces = spaces.len();  // now usize type
    println!("spaces = {}", spaces);
}
```

### Key Difference from C/Python
```rust
// In C:    int x = 5; x = 10;     → mutable by default
// In Rust: let x = 5; x = 10;     → ❌ ERROR (immutable by default)
// In Rust: let mut x = 5; x = 10; → ✅ explicitly mutable
```

---

## 3. Data Types

### Scalar Types (Single Values)
```rust
fn main() {
    // ========== INTEGERS ==========
    let a: i8  = -128;          // signed 8-bit  (-128 to 127)
    let b: i16 = -32_768;       // signed 16-bit
    let c: i32 = 42;            // signed 32-bit (DEFAULT)
    let d: i64 = 1_000_000;     // signed 64-bit (underscores for readability)
    let e: i128 = 99;           // signed 128-bit

    let f: u8  = 255;           // unsigned 8-bit (0 to 255)
    let g: u16 = 65_535;        // unsigned 16-bit
    let h: u32 = 100;           // unsigned 32-bit
    let i: u64 = 999;           // unsigned 64-bit
    let j: u128 = 42;           // unsigned 128-bit

    let k: isize = 10;          // platform dependent (32 or 64 bit)
    let l: usize = 10;          // platform dependent (used for indexing)

    // ========== FLOATS ==========
    let x: f32 = 3.14;          // 32-bit float
    let y: f64 = 2.71828;       // 64-bit float (DEFAULT)

    // ========== BOOLEAN ==========
    let is_active: bool = true;
    let is_deleted = false;      // type inferred

    // ========== CHARACTER ==========
    let letter: char = 'A';     // single quotes, 4 bytes (Unicode)
    let emoji: char = '🦀';     // supports emoji!
    let heart = '❤';

    // ========== NUMBER LITERALS ==========
    let decimal = 98_222;       // 98222
    let hex = 0xff;             // 255
    let octal = 0o77;           // 63
    let binary = 0b1111_0000;   // 240
    let byte = b'A';            // 65 (u8 only)

    println!("int: {}, float: {}, bool: {}, char: {}", c, y, is_active, emoji);
}
```

### Compound Types
```rust
fn main() {
    // ========== TUPLES (fixed size, mixed types) ==========
    let tup: (i32, f64, char) = (500, 6.4, 'A');

    // Accessing tuple elements
    let first = tup.0;          // dot notation
    let second = tup.1;
    let third = tup.2;
    println!("Tuple: {}, {}, {}", first, second, third);

    // Destructuring
    let (x, y, z) = tup;
    println!("Destructured: {}, {}, {}", x, y, z);

    // Unit tuple (empty tuple)
    let unit: () = ();

    // ========== ARRAYS (fixed size, same type) ==========
    let arr: [i32; 5] = [1, 2, 3, 4, 5];   // [type; length]
    let first = arr[0];         // indexing starts at 0
    let last = arr[4];
    println!("Array: {} to {}", first, last);

    // Initialize with same value
    let zeros = [0; 10];        // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    println!("Length: {}", zeros.len());

    // arr[10];                 // ❌ Runtime panic! (Rust checks bounds)
}
```

### Type Diagram
```
Rust Data Types
├── Scalar (single value)
│   ├── Integer:   i8, i16, i32, i64, i128, isize
│   │              u8, u16, u32, u64, u128, usize
│   ├── Float:     f32, f64
│   ├── Boolean:   bool
│   └── Character: char
│
└── Compound (multiple values)
    ├── Tuple:     (i32, f64, char)
    └── Array:     [i32; 5]
```

---

## 4. Functions

```rust
// ========== BASIC FUNCTION ==========
fn greet() {
    println!("Hello!");
}

// ========== FUNCTION WITH PARAMETERS ==========
fn greet_person(name: &str) {       // parameter types are REQUIRED
    println!("Hello, {}!", name);
}

// ========== MULTIPLE PARAMETERS ==========
fn add(a: i32, b: i32) {
    println!("{} + {} = {}", a, b, a + b);
}

// ========== FUNCTION WITH RETURN VALUE ==========
fn multiply(a: i32, b: i32) -> i32 {   // -> specifies return type
    a * b                                // no semicolon = return value (expression)
}

// You can also use `return` keyword explicitly
fn divide(a: f64, b: f64) -> f64 {
    if b == 0.0 {
        return 0.0;          // early return with `return` keyword
    }
    a / b                    // implicit return (last expression)
}

// ========== MULTIPLE RETURN VALUES (using tuple) ==========
fn swap(a: i32, b: i32) -> (i32, i32) {
    (b, a)
}

fn main() {
    greet();
    greet_person("Alice");
    add(5, 3);

    let product = multiply(4, 5);
    println!("4 × 5 = {}", product);

    let result = divide(10.0, 3.0);
    println!("10 / 3 = {:.2}", result);    // .2 = 2 decimal places

    let (x, y) = swap(1, 2);
    println!("Swapped: {}, {}", x, y);
}
```

### Statements vs Expressions
```rust
fn main() {
    // STATEMENT: performs action, returns nothing
    let x = 5;              // this is a statement

    // EXPRESSION: evaluates to a value
    let y = {
        let temp = 3;
        temp + 1             // ⚠️ NO semicolon = expression (returns 4)
    };
    println!("y = {}", y);  // y = 4

    // If semicolon is added, it becomes a statement (returns nothing)
    let z = {
        let temp = 3;
        temp + 1;            // semicolon makes it a statement → returns ()
    };
    // z is now () (unit type)
}
```

---

## 5. Printing & Formatting

```rust
fn main() {
    // ========== BASIC PRINTING ==========
    println!("Hello, World!");          // with newline
    print!("No newline");              // without newline
    eprintln!("This goes to stderr");  // error output

    // ========== PLACEHOLDERS ==========
    let name = "Alice";
    let age = 30;

    println!("Name: {}, Age: {}", name, age);         // positional
    println!("Name: {0}, Age: {1}, Name again: {0}", name, age); // indexed
    println!("Name: {name}, Age: {age}");              // named (Rust 1.58+)

    // ========== FORMATTING ==========
    let pi = 3.14159265;

    println!("Pi: {:.2}", pi);           // 2 decimal places → 3.14
    println!("Pi: {:.4}", pi);           // 4 decimal places → 3.1416
    println!("Padded: {:10}", 42);       // right-aligned, width 10
    println!("Padded: {:<10}", 42);      // left-aligned
    println!("Padded: {:^10}", 42);      // center-aligned
    println!("Padded: {:0>5}", 42);      // zero-padded → 00042

    // ========== NUMBER FORMATS ==========
    println!("Binary:  {:b}", 42);       // 101010
    println!("Octal:   {:o}", 42);       // 52
    println!("Hex:     {:x}", 255);      // ff
    println!("Hex:     {:X}", 255);      // FF
    println!("Scientific: {:e}", 1000.0);// 1e3

    // ========== DEBUG PRINTING ==========
    let arr = [1, 2, 3, 4, 5];
    println!("Debug: {:?}", arr);        // Debug format
    println!("Pretty: {:#?}", arr);      // Pretty debug format
}
```

---

## 6. Control Flow

### If / Else
```rust
fn main() {
    let number = 7;

    // ========== BASIC IF/ELSE ==========
    if number > 0 {
        println!("Positive");
    } else if number < 0 {
        println!("Negative");
    } else {
        println!("Zero");
    }

    // ========== IF AS EXPRESSION (like ternary) ==========
    let status = if number > 0 { "positive" } else { "not positive" };
    println!("Number is {}", status);

    // ⚠️ Condition MUST be bool (no truthy/falsy like Python)
    // if number { }          // ❌ ERROR! expected bool, got integer
    if number != 0 {          // ✅ Must be explicit
        println!("Not zero");
    }
}
```

### Loops
```rust
fn main() {
    // ========== LOOP (infinite loop) ==========
    let mut counter = 0;
    loop {
        counter += 1;
        if counter == 5 {
            break;             // exit the loop
        }
        if counter == 3 {
            continue;          // skip rest, go to next iteration
        }
        println!("loop counter: {}", counter);
    }
    // Prints: 1, 2, 4

    // ========== LOOP WITH RETURN VALUE ==========
    let mut num = 0;
    let result = loop {
        num += 1;
        if num == 10 {
            break num * 2;     // break WITH a value
        }
    };
    println!("Result: {}", result);  // 20

    // ========== WHILE LOOP ==========
    let mut count = 3;
    while count > 0 {
        println!("{}!", count);
        count -= 1;
    }
    println!("Liftoff!");

    // ========== FOR LOOP (most common) ==========
    // Range
    for i in 1..5 {            // 1, 2, 3, 4  (exclusive end)
        print!("{} ", i);
    }
    println!();

    for i in 1..=5 {           // 1, 2, 3, 4, 5  (inclusive end)
        print!("{} ", i);
    }
    println!();

    // Iterating over array
    let fruits = ["apple", "banana", "cherry"];
    for fruit in fruits {
        println!("I like {}", fruit);
    }

    // With index
    for (index, fruit) in fruits.iter().enumerate() {
        println!("{}: {}", index, fruit);
    }

    // Reverse
    for i in (1..=5).rev() {
        print!("{} ", i);      // 5 4 3 2 1
    }
    println!();

    // ========== LOOP LABELS (nested loops) ==========
    'outer: for i in 0..3 {
        'inner: for j in 0..3 {
            if i == 1 && j == 1 {
                break 'outer;  // breaks the OUTER loop
            }
            println!("i={}, j={}", i, j);
        }
    }
}
```

---

## 7. Strings

```rust
fn main() {
    // ========== TWO STRING TYPES ==========

    // &str - string slice (fixed, usually hardcoded, stored on stack/binary)
    let greeting: &str = "Hello, World!";

    // String - growable, heap-allocated, owned
    let mut name: String = String::from("Alice");

    // ========== CREATING STRINGS ==========
    let s1 = String::new();                    // empty String
    let s2 = String::from("Hello");            // from literal
    let s3 = "Hello".to_string();              // convert &str to String
    let s4 = format!("{} {}", "Hello", "World"); // format macro

    // ========== COMMON OPERATIONS ==========
    let mut s = String::from("Hello");

    // Append
    s.push(' ');                   // push single char
    s.push_str("World");          // push string slice
    println!("{}", s);             // "Hello World"

    // Length
    println!("Length: {}", s.len());        // bytes
    println!("Chars: {}", s.chars().count()); // characters

    // Check content
    println!("Empty? {}", s.is_empty());
    println!("Contains 'World'? {}", s.contains("World"));
    println!("Starts with 'Hello'? {}", s.starts_with("Hello"));

    // Replace
    let new_s = s.replace("World", "Rust");
    println!("{}", new_s);         // "Hello Rust"

    // Trim whitespace
    let padded = "  Hello  ";
    println!("'{}'", padded.trim());   // 'Hello'

    // Split
    let sentence = "one,two,three";
    for word in sentence.split(',') {
        println!("{}", word);
    }

    // To uppercase/lowercase
    println!("{}", "hello".to_uppercase());  // HELLO
    println!("{}", "HELLO".to_lowercase());  // hello

    // ========== STRING CONCATENATION ==========
    let s1 = String::from("Hello");
    let s2 = String::from(" World");

    // Method 1: + operator (s1 is MOVED, can't use after)
    let s3 = s1 + &s2;        // s1 moved here, s2 borrowed
    // println!("{}", s1);     // ❌ ERROR: s1 was moved
    println!("{}", s3);        // ✅ "Hello World"

    // Method 2: format! macro (nothing is moved)
    let s4 = String::from("Hello");
    let s5 = String::from(" World");
    let s6 = format!("{}{}", s4, s5);
    println!("{}", s4);        // ✅ still valid
    println!("{}", s6);

    // ========== ITERATING OVER CHARACTERS ==========
    for c in "Hello".chars() {
        print!("{} ", c);      // H e l l o
    }
    println!();

    // ========== STRING SLICING ==========
    let hello = String::from("Hello, World!");
    let slice = &hello[0..5];  // "Hello"  (byte indices!)
    println!("{}", slice);
}
```

### String Types Cheat Sheet
```
┌──────────────┬────────────────────────────────────┐
│    &str      │         String                     │
├──────────────┼────────────────────────────────────┤
│ Immutable    │ Mutable (with mut)                 │
│ Fixed size   │ Growable                           │
│ Borrowed     │ Owned                              │
│ Stack/binary │ Heap allocated                     │
│ "hello"      │ String::from("hello")              │
│ Fast, cheap  │ Flexible, can modify               │
└──────────────┴────────────────────────────────────┘
```

---

## 8. Ownership (⭐ Most Important Concept!)

```rust
fn main() {
    // ========== THE 3 OWNERSHIP RULES ==========
    // 1. Each value has ONE owner
    // 2. There can only be ONE owner at a time
    // 3. When the owner goes out of scope, the value is dropped

    // ========== MOVE SEMANTICS ==========
    let s1 = String::from("hello");
    let s2 = s1;              // s1 is MOVED to s2

    // println!("{}", s1);    // ❌ ERROR: s1 is no longer valid
    println!("{}", s2);       // ✅ s2 owns the value

    // ========== CLONE (deep copy) ==========
    let s3 = String::from("hello");
    let s4 = s3.clone();     // deep copy — both are valid

    println!("{}", s3);       // ✅ still valid
    println!("{}", s4);       // ✅ independent copy

    // ========== COPY (stack-only types) ==========
    // Simple types like integers implement Copy trait
    let x = 5;
    let y = x;               // COPY (not move) — integers are on stack

    println!("{}", x);        // ✅ still valid!
    println!("{}", y);        // ✅ independent copy

    // Types that implement Copy: i32, f64, bool, char, tuples of Copy types

    // ========== OWNERSHIP WITH FUNCTIONS ==========
    let s = String::from("hello");
    take_ownership(s);        // s is MOVED into the function
    // println!("{}", s);     // ❌ ERROR: s was moved

    let n = 42;
    make_copy(n);             // n is COPIED (i32 implements Copy)
    println!("{}", n);        // ✅ still valid
}

fn take_ownership(text: String) {
    println!("Got: {}", text);
}   // `text` is dropped here, memory freed

fn make_copy(num: i32) {
    println!("Got: {}", num);
}   // `num` goes out of scope, nothing special (stack)
```

### Ownership Visualized
```
MOVE:
  let s1 = String::from("hello");
  
  Stack          Heap
  s1: ptr -----> "hello"
  
  let s2 = s1;   // MOVE
  
  Stack          Heap
  s1: INVALID
  s2: ptr -----> "hello"


CLONE:
  let s3 = s1.clone();
  
  Stack          Heap
  s1: ptr -----> "hello"
  s3: ptr -----> "hello" (separate copy)
```

---

## 9. Borrowing & References

```rust
fn main() {
    // ========== IMMUTABLE REFERENCE (&T) ==========
    let s1 = String::from("hello");

    let len = calculate_length(&s1);   // BORROW s1 (don't take ownership)
    println!("'{}' has length {}", s1, len);  // ✅ s1 still valid!

    // ========== MUTABLE REFERENCE (&mut T) ==========
    let mut s2 = String::from("hello");
    change(&mut s2);                   // mutable borrow
    println!("{}", s2);                // "hello, world"

    // ========== BORROWING RULES ==========

    // Rule 1: You can have MANY immutable references
    let s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    let r3 = &s;
    println!("{}, {}, {}", r1, r2, r3);  // ✅ all fine

    // Rule 2: You can have only ONE mutable reference
    let mut s = String::from("hello");
    let r1 = &mut s;
    // let r2 = &mut s;              // ❌ ERROR: can't borrow mutably twice
    println!("{}", r1);

    // Rule 3: Can't mix mutable and immutable references
    let mut s = String::from("hello");
    let r1 = &s;         // immutable borrow
    let r2 = &s;         // immutable borrow
    // let r3 = &mut s;  // ❌ ERROR: can't borrow mutably while immutably borrowed
    println!("{}, {}", r1, r2);

    // After last use of r1, r2, you CAN borrow mutably
    let r3 = &mut s;     // ✅ r1, r2 no longer used after this
    println!("{}", r3);
}

fn calculate_length(s: &String) -> usize {   // borrows, doesn't own
    s.len()
}   // s goes out of scope, but doesn't drop (it doesn't own the value)

fn change(s: &mut String) {                  // mutable borrow
    s.push_str(", world");
}
```

### Borrowing Rules Summary
```
╔══════════════════════════════════════════════════╗
║              BORROWING RULES                     ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  At any given time, you can have EITHER:         ║
║    ✅ ONE mutable reference    (&mut T)          ║
║    ✅ ANY number of immutable references (&T)    ║
║                                                  ║
║  But NOT both at the same time!                  ║
║                                                  ║
║  References must always be valid (no dangling)   ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

---

## 10. Structs

```rust
// ========== DEFINING A STRUCT ==========
struct User {
    username: String,
    email: String,
    age: u32,
    active: bool,
}

// ========== IMPLEMENTING METHODS ==========
impl User {
    // Associated function (like a constructor) — no &self
    fn new(username: &str, email: &str, age: u32) -> User {
        User {
            username: String::from(username),
            email: String::from(email),
            age,               // shorthand when field name = variable name
            active: true,
        }
    }

    // Method — takes &self (immutable reference to instance)
    fn summary(&self) -> String {
        format!("{} ({}) - age {}", self.username, self.email, self.age)
    }

    // Method that modifies — takes &mut self
    fn deactivate(&mut self) {
        self.active = false;
    }

    // Method that checks
    fn is_adult(&self) -> bool {
        self.age >= 18
    }
}

// ========== TUPLE STRUCTS ==========
struct Color(u8, u8, u8);
struct Point(f64, f64, f64);

// ========== UNIT STRUCT ==========
struct AlwaysEqual;

fn main() {
    // Creating an instance
    let mut user1 = User::new("alice", "alice@example.com", 25);
    println!("{}", user1.summary());
    println!("Adult? {}", user1.is_adult());

    // Modifying
    user1.deactivate();
    user1.age = 26;

    // Struct update syntax (create from another)
    let user2 = User {
        username: String::from("bob"),
        email: String::from("bob@example.com"),
        ..user1                // rest of fields from user1
    };

    // Tuple structs
    let red = Color(255, 0, 0);
    println!("Red: {}, {}, {}", red.0, red.1, red.2);

    let origin = Point(0.0, 0.0, 0.0);
}
```

### Debug Printing Structs
```rust
#[derive(Debug)]               // Add this to enable {:?} printing
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    fn is_square(&self) -> bool {
        self.width == self.height
    }
}

fn main() {
    let rect = Rectangle { width: 10.0, height: 5.0 };
    println!("{:?}", rect);        // Debug print
    println!("{:#?}", rect);       // Pretty debug print
    println!("Area: {}", rect.area());
    println!("Perimeter: {}", rect.perimeter());
    println!("Square? {}", rect.is_square());
}
```

---

## 11. Enums & Pattern Matching

```rust
// ========== BASIC ENUM ==========
enum Direction {
    North,
    South,
    East,
    West,
}

// ========== ENUM WITH DATA ==========
enum IpAddress {
    V4(u8, u8, u8, u8),
    V6(String),
}

// ========== ENUM WITH DIFFERENT TYPES ==========
enum Message {
    Quit,                       // no data
    Echo(String),               // String data
    Move { x: i32, y: i32 },   // named fields (like struct)
    Color(u8, u8, u8),         // tuple data
}

// Implement methods on enums
impl Message {
    fn process(&self) {
        match self {
            Message::Quit => println!("Quitting"),
            Message::Echo(text) => println!("Echo: {}", text),
            Message::Move { x, y } => println!("Move to ({}, {})", x, y),
            Message::Color(r, g, b) => println!("Color: ({}, {}, {})", r, g, b),
        }
    }
}

fn main() {
    // ========== USING ENUMS ==========
    let dir = Direction::North;
    let home = IpAddress::V4(127, 0, 0, 1);
    let loopback = IpAddress::V6(String::from("::1"));

    // ========== MATCH (exhaustive pattern matching) ==========
    match dir {
        Direction::North => println!("Going North"),
        Direction::South => println!("Going South"),
        Direction::East  => println!("Going East"),
        Direction::West  => println!("Going West"),
    }   // Must handle ALL variants!

    // Match with values
    let number = 7;
    let description = match number {
        1 => "one",
        2 => "two",
        3..=9 => "between three and nine",   // range pattern
        10 | 20 => "ten or twenty",          // multiple patterns
        _ => "something else",               // _ = default/wildcard
    };
    println!("{} is {}", number, description);

    // ========== OPTION<T> (Rust's null replacement) ==========
    // enum Option<T> {
    //     Some(T),     // has a value
    //     None,        // no value
    // }

    let some_number: Option<i32> = Some(42);
    let no_number: Option<i32> = None;

    // You MUST handle both cases
    match some_number {
        Some(value) => println!("Got: {}", value),
        None => println!("Got nothing"),
    }

    // Using .unwrap() (panics if None — use carefully!)
    let x: Option<i32> = Some(10);
    println!("{}", x.unwrap());         // 10

    // Using .unwrap_or() (safe default)
    let y: Option<i32> = None;
    println!("{}", y.unwrap_or(0));     // 0

    // ========== IF LET (shorthand for single pattern) ==========
    let value = Some(42);

    // Instead of full match:
    if let Some(v) = value {
        println!("Got value: {}", v);
    } else {
        println!("No value");
    }

    // ========== MESSAGES ==========
    let msg = Message::Echo(String::from("Hello!"));
    msg.process();
}
```

---

## 12. Vectors (Dynamic Arrays)

```rust
fn main() {
    // ========== CREATING VECTORS ==========
    let v1: Vec<i32> = Vec::new();        // empty vector
    let v2 = vec![1, 2, 3, 4, 5];        // vec! macro
    let v3 = vec![0; 10];                 // 10 zeros

    // ========== ADDING ELEMENTS ==========
    let mut v = Vec::new();
    v.push(1);
    v.push(2);
    v.push(3);
    println!("{:?}", v);                  // [1, 2, 3]

    // ========== ACCESSING ELEMENTS ==========
    let third = v[2];                     // direct access (panics if out of bounds)
    let third = v.get(2);                 // returns Option<&T> (safe)

    match v.get(10) {
        Some(value) => println!("Got: {}", value),
        None => println!("Index out of bounds"),
    }

    // ========== MODIFYING ==========
    v[0] = 10;                            // modify element
    v.pop();                              // remove last element → returns Option<T>
    v.insert(1, 99);                      // insert at index
    v.remove(0);                          // remove at index

    println!("{:?}", v);

    // ========== ITERATING ==========
    let scores = vec![90, 85, 92, 78, 95];

    // Immutable iteration
    for score in &scores {
        println!("Score: {}", score);
    }

    // Mutable iteration
    let mut nums = vec![1, 2, 3, 4, 5];
    for n in &mut nums {
        *n *= 2;                          // dereference to modify
    }
    println!("{:?}", nums);               // [2, 4, 6, 8, 10]

    // ========== USEFUL METHODS ==========
    let v = vec![3, 1, 4, 1, 5, 9, 2, 6];

    println!("Length: {}", v.len());
    println!("Empty? {}", v.is_empty());
    println!("Contains 5? {}", v.contains(&5));

    let mut v_sorted = v.clone();
    v_sorted.sort();
    println!("Sorted: {:?}", v_sorted);

    // ========== VECTOR WITH ENUM (mixed types) ==========
    enum Cell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        Cell::Int(42),
        Cell::Float(3.14),
        Cell::Text(String::from("hello")),
    ];
}
```

---

## 13. HashMap

```rust
use std::collections::HashMap;

fn main() {
    // ========== CREATING ==========
    let mut scores: HashMap<String, i32> = HashMap::new();

    // ========== INSERTING ==========
    scores.insert(String::from("Alice"), 95);
    scores.insert(String::from("Bob"), 87);
    scores.insert(String::from("Charlie"), 92);

    println!("{:?}", scores);

    // ========== ACCESSING ==========
    let alice_score = scores.get("Alice");     // returns Option<&V>
    match alice_score {
        Some(score) => println!("Alice: {}", score),
        None => println!("Alice not found"),
    }

    // ========== ITERATING ==========
    for (name, score) in &scores {
        println!("{}: {}", name, score);
    }

    // ========== UPDATING ==========
    // Overwrite
    scores.insert(String::from("Alice"), 100);

    // Insert only if key doesn't exist
    scores.entry(String::from("Dave")).or_insert(80);
    scores.entry(String::from("Alice")).or_insert(50);  // won't overwrite
    println!("Alice: {}", scores["Alice"]);              // still 100

    // Update based on old value
    let text = "hello world hello rust hello";
    let mut word_count = HashMap::new();
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);
        *count += 1;
    }
    println!("{:?}", word_count);

    // ========== REMOVING ==========
    scores.remove("Bob");

    // ========== CHECKING ==========
    println!("Contains Alice? {}", scores.contains_key("Alice"));
    println!("Length: {}", scores.len());
}
```

---

## 14. Error Handling

```rust
use std::fs::File;
use std::io::{self, Read};

fn main() {
    // ========== panic! (unrecoverable errors) ==========
    // panic!("Something went terribly wrong!");  // crashes the program

    // ========== Result<T, E> (recoverable errors) ==========
    // enum Result<T, E> {
    //     Ok(T),      // success
    //     Err(E),     // error
    // }

    // ========== HANDLING WITH MATCH ==========
    let file_result = File::open("hello.txt");

    let file = match file_result {
        Ok(f) => f,
        Err(error) => {
            println!("Error opening file: {}", error);
            return;
        }
    };

    // ========== SHORTCUT: unwrap() and expect() ==========
    // let f = File::open("hello.txt").unwrap();        // panics with generic message
    // let f = File::open("hello.txt").expect("Failed to open file"); // panics with custom message

    // ========== SHORTCUT: ? operator (propagate errors) ==========
    match read_file_content("hello.txt") {
        Ok(content) => println!("File content: {}", content),
        Err(e) => println!("Error: {}", e),
    }

    // ========== PARSING WITH ERROR HANDLING ==========
    let number: Result<i32, _> = "42".parse();
    let number: Result<i32, _> = "not a number".parse();

    match "42".parse::<i32>() {
        Ok(n) => println!("Parsed: {}", n),
        Err(e) => println!("Parse error: {}", e),
    }

    // unwrap_or for defaults
    let n: i32 = "abc".parse().unwrap_or(0);
    println!("Parsed or default: {}", n);   // 0
}

// ========== FUNCTION THAT RETURNS Result ==========
fn read_file_content(filename: &str) -> Result<String, io::Error> {
    let mut file = File::open(filename)?;   // ? returns Err early if fails
    let mut content = String::new();
    file.read_to_string(&mut content)?;     // ? returns Err early if fails
    Ok(content)                              // wrap success in Ok
}

// Shorter version
fn read_file_short(filename: &str) -> Result<String, io::Error> {
    std::fs::read_to_string(filename)
}
```

### Error Handling Decision Tree
```
Should I use panic! or Result?
│
├── Is it an example/prototype/test?
│   └── YES → unwrap() / expect() / panic! is fine
│
├── Could the caller handle this error?
│   └── YES → Return Result<T, E>
│
├── Is it truly unrecoverable?
│   └── YES → panic!
│
└── Library code?
    └── Almost always return Result<T, E>
```

---

## 15. User Input

```rust
use std::io;

fn main() {
    // ========== BASIC INPUT ==========
    println!("What's your name?");

    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read line");

    let name = name.trim();    // remove newline
    println!("Hello, {}!", name);

    // ========== INPUT WITH PARSING ==========
    println!("Enter a number:");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let number: i32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Not a valid number!");
            return;
        }
    };

    println!("You entered: {}", number);

    // ========== LOOP UNTIL VALID INPUT ==========
    let age: u32 = loop {
        println!("Enter your age:");
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read");

        match input.trim().parse() {
            Ok(num) => break num,
            Err(_) => println!("Please enter a valid number!"),
        }
    };

    println!("Your age: {}", age);
}
```

---

## 16. Complete Practice Programs

### Program 1: Temperature Converter
```rust
use std::io;

fn main() {
    println!("=== Temperature Converter ===");
    println!("1. Celsius to Fahrenheit");
    println!("2. Fahrenheit to Celsius");
    print!("Choose (1 or 2): ");

    let choice = read_input();
    print!("Enter temperature: ");
    let temp: f64 = read_input();

    match choice {
        1 => {
            let f = temp * 9.0 / 5.0 + 32.0;
            println!("{:.1}°C = {:.1}°F", temp, f);
        }
        2 => {
            let c = (temp - 32.0) * 5.0 / 9.0;
            println!("{:.1}°F = {:.1}°C", temp, c);
        }
        _ => println!("Invalid choice!"),
    }
}

fn read_input<T: std::str::FromStr>() -> T {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read");
    input.trim().parse().ok().expect("Invalid input")
}
```

### Program 2: Number Guessing Game
```rust
use std::io;
use std::cmp::Ordering;

fn main() {
    println!("=== Guess the Number! ===");

    // Simple random without external crate
    let secret = simple_random(1, 100);
    let mut attempts = 0;

    loop {
        println!("\nEnter your guess (1-100):");

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read");

        let guess: u32 = match input.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Please enter a valid number!");
                continue;
            }
        };

        attempts += 1;

        match guess.cmp(&secret) {
            Ordering::Less => println!("📈 Too low!"),
            Ordering::Greater => println!("📉 Too high!"),
            Ordering::Equal => {
                println!("🎉 Correct! You guessed in {} attempts!", attempts);
                break;
            }
        }
    }
}

fn simple_random(min: u32, max: u32) -> u32 {
    use std::time::SystemTime;
    let seed = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .unwrap()
        .subsec_nanos();
    min + (seed % (max - min + 1))
}
```

### Program 3: Student Grade Manager
```rust
use std::collections::HashMap;

#[derive(Debug)]
struct Student {
    name: String,
    grades: Vec<f64>,
}

impl Student {
    fn new(name: &str) -> Student {
        Student {
            name: String::from(name),
            grades: Vec::new(),
        }
    }

    fn add_grade(&mut self, grade: f64) {
        self.grades.push(grade);
    }

    fn average(&self) -> f64 {
        if self.grades.is_empty() {
            return 0.0;
        }
        let sum: f64 = self.grades.iter().sum();
        sum / self.grades.len() as f64
    }

    fn highest(&self) -> f64 {
        self.grades.iter().cloned().fold(f64::MIN, f64::max)
    }

    fn lowest(&self) -> f64 {
        self.grades.iter().cloned().fold(f64::MAX, f64::min)
    }

    fn letter_grade(&self) -> &str {
        match self.average() as u32 {
            90..=100 => "A",
            80..=89  => "B",
            70..=79  => "C",
            60..=69  => "D",
            _        => "F",
        }
    }

    fn display(&self) {
        println!("Student: {}", self.name);
        println!("  Grades: {:?}", self.grades);
        println!("  Average: {:.1}", self.average());
        println!("  Highest: {:.1}", self.highest());
        println!("  Lowest: {:.1}", self.lowest());
        println!("  Letter: {}", self.letter_grade());
        println!();
    }
}

fn main() {
    let mut students: Vec<Student> = Vec::new();

    let mut alice = Student::new("Alice");
    alice.add_grade(92.0);
    alice.add_grade(88.0);
    alice.add_grade(95.0);
    alice.add_grade(91.0);

    let mut bob = Student::new("Bob");
    bob.add_grade(78.0);
    bob.add_grade(82.0);
    bob.add_grade(75.0);
    bob.add_grade(80.0);

    let mut charlie = Student::new("Charlie");
    charlie.add_grade(95.0);
    charlie.add_grade(98.0);
    charlie.add_grade(92.0);
    charlie.add_grade(97.0);

    students.push(alice);
    students.push(bob);
    students.push(charlie);

    println!("=== Student Grade Report ===\n");
    for student in &students {
        student.display();
    }

    // Find top student
    let top = students
        .iter()
        .max_by(|a, b| a.average().partial_cmp(&b.average()).unwrap())
        .unwrap();
    println!("🏆 Top Student: {} ({:.1})", top.name, top.average());

    // Class average
    let class_avg: f64 = students.iter().map(|s| s.average()).sum::<f64>()
        / students.len() as f64;
    println!("📊 Class Average: {:.1}", class_avg);
}
```

---

## 📋 Quick Reference Cheat Sheet

```
╔══════════════════════════════════════════════════════════╗
║                  RUST QUICK REFERENCE                    ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  VARIABLES                                               ║
║    let x = 5;              // immutable                  ║
║    let mut x = 5;          // mutable                    ║
║    const X: i32 = 5;       // constant                   ║
║                                                          ║
║  FUNCTIONS                                               ║
║    fn name(param: Type) -> ReturnType { body }           ║
║                                                          ║
║  OWNERSHIP                                               ║
║    let s2 = s1;            // move                       ║
║    let s2 = s1.clone();    // deep copy                  ║
║    let r = &s;             // immutable borrow           ║
║    let r = &mut s;         // mutable borrow             ║
║                                                          ║
║  STRUCTS                                                 ║
║    struct Name { field: Type }                           ║
║    impl Name { fn method(&self) {} }                     ║
║                                                          ║
║  ENUMS                                                   ║
║    enum Name { Variant1, Variant2(Type) }                ║
║    match value { pattern => result }                     ║
║                                                          ║
║  OPTION & RESULT                                         ║
║    Option<T>  → Some(T) | None                           ║
║    Result<T,E> → Ok(T) | Err(E)                         ║
║                                                          ║
║  COLLECTIONS                                             ║
║    Vec<T>           → vec![1, 2, 3]                      ║
║    HashMap<K, V>    → HashMap::new()                     ║
║    String           → String::from("hello")              ║
║                                                          ║
║  PRINTING                                                ║
║    println!("{}", val);       // Display                  ║
║    println!("{:?}", val);     // Debug                    ║
║    println!("{:#?}", val);    // Pretty Debug             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

---

## ✅ What To Do Next

```
1. 📖 Read "The Rust Book" Chapters 1-8 alongside this guide
2. 🏋️ Do Rustlings exercises (install: cargo install rustlings)
3. 💻 Type out every example above — don't copy-paste!
4. 🔨 Build the practice projects
5. 🐛 Intentionally break code to understand error messages
6. 📝 Move to Phase 2 of the roadmap (Iterators, Traits, Generics)
```

> **Golden Rule: The compiler is your best teacher. Read every error message carefully — Rust has the best error messages of any language!** 🦀

# 🦀 Rust: Functions, "Classes" & Data Structures — Complete Guide

> **Note:** Rust has NO classes. It uses **Structs + Impl + Traits** instead.

---

## PART 1: FUNCTIONS (Complete Deep Dive)

### 1.1 Basic Function Anatomy

```rust
//  keyword  name     parameters       return type
//    ↓       ↓          ↓                ↓
      fn    add    (a: i32, b: i32)   -> i32    {
          a + b    // ← return value (no semicolon = expression)
      }
```

### 1.2 All Function Types

```rust
// ========== 1. NO PARAMS, NO RETURN ==========
fn greet() {
    println!("Hello!");
}

// ========== 2. WITH PARAMS, NO RETURN ==========
fn print_sum(a: i32, b: i32) {
    println!("{} + {} = {}", a, b, a + b);
}

// ========== 3. WITH RETURN VALUE ==========
fn add(a: i32, b: i32) -> i32 {
    a + b                   // implicit return (no semicolon)
}

// ========== 4. EXPLICIT RETURN ==========
fn divide(a: f64, b: f64) -> f64 {
    if b == 0.0 {
        return 0.0;         // early return with `return` keyword
    }
    a / b                   // implicit return for last expression
}

// ========== 5. MULTIPLE RETURN VALUES (tuple) ==========
fn min_max(list: &[i32]) -> (i32, i32) {
    let mut min = list[0];
    let mut max = list[0];
    for &val in list {
        if val < min { min = val; }
        if val > max { max = val; }
    }
    (min, max)
}

// ========== 6. RETURNING NOTHING EXPLICITLY ==========
fn do_something() -> () {   // () is "unit type" (like void)
    println!("Done");
}

fn main() {
    greet();
    print_sum(3, 4);

    let result = add(5, 3);
    println!("Sum: {}", result);

    let ratio = divide(10.0, 3.0);
    println!("Ratio: {:.2}", ratio);

    let (min, max) = min_max(&[3, 1, 4, 1, 5, 9]);
    println!("Min: {}, Max: {}", min, max);
}
```

### 1.3 Functions with References (Borrowing)

```rust
// ========== IMMUTABLE REFERENCE ==========
fn length(s: &String) -> usize {
    s.len()
    // s is borrowed, caller keeps ownership
}

// ========== MUTABLE REFERENCE ==========
fn add_exclamation(s: &mut String) {
    s.push_str("!");
    // modifies the original string
}

// ========== STRING SLICE (preferred over &String) ==========
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return &s[0..i];
        }
    }
    s
}

// ========== TAKING OWNERSHIP ==========
fn consume_string(s: String) {
    println!("Consumed: {}", s);
}   // s is dropped here

// ========== RETURNING OWNERSHIP ==========
fn create_greeting(name: &str) -> String {
    format!("Hello, {}!", name)    // returns owned String
}

fn main() {
    let s = String::from("Hello World");

    // Borrowing (original still usable)
    println!("Length: {}", length(&s));
    println!("First word: {}", first_word(&s));
    println!("Still have s: {}", s);    // ✅ still valid

    // Mutable borrowing
    let mut s2 = String::from("Hello");
    add_exclamation(&mut s2);
    println!("{}", s2);                  // "Hello!"

    // Ownership transfer
    consume_string(s);
    // println!("{}", s);               // ❌ ERROR: s was moved

    // Receiving ownership
    let greeting = create_greeting("Alice");
    println!("{}", greeting);
}
```

### 1.4 Generic Functions

```rust
// ========== BASIC GENERIC ==========
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// ========== MULTIPLE GENERIC TYPES ==========
fn pair_to_string<T: std::fmt::Display, U: std::fmt::Display>(a: T, b: U) -> String {
    format!("({}, {})", a, b)
}

// ========== WHERE CLAUSE (cleaner syntax) ==========
fn print_if_long<T>(item: &T)
where
    T: std::fmt::Display + std::fmt::Debug,
{
    println!("Display: {}", item);
    println!("Debug: {:?}", item);
}

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    println!("Largest: {}", largest(&numbers));

    let chars = vec!['a', 'z', 'm', 'b'];
    println!("Largest: {}", largest(&chars));

    println!("{}", pair_to_string(42, "hello"));
    print_if_long(&"Hello World");
}
```

### 1.5 Closures (Anonymous Functions)

```rust
fn main() {
    // ========== BASIC CLOSURES ==========
    let add = |a: i32, b: i32| -> i32 { a + b };
    let add_short = |a, b| a + b;          // types inferred
    let greet = || println!("Hello!");      // no parameters
    let square = |x| x * x;                // single param

    println!("{}", add(3, 4));              // 7
    println!("{}", add_short(3, 4));        // 7
    greet();
    println!("{}", square(5));              // 25

    // ========== CLOSURES CAPTURE VARIABLES ==========
    let name = String::from("Alice");
    let greet_name = || println!("Hello, {}!", name);   // captures `name`
    greet_name();
    println!("Still have name: {}", name);   // ✅ immutable borrow

    // ========== MUTABLE CAPTURE ==========
    let mut count = 0;
    let mut increment = || {
        count += 1;                         // captures `count` mutably
        println!("Count: {}", count);
    };
    increment();    // Count: 1
    increment();    // Count: 2
    increment();    // Count: 3

    // ========== MOVE CLOSURE (takes ownership) ==========
    let data = vec![1, 2, 3];
    let print_data = move || {              // `move` forces ownership transfer
        println!("{:?}", data);
    };
    print_data();
    // println!("{:?}", data);              // ❌ data was moved

    // ========== CLOSURES WITH ITERATORS ==========
    let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    let evens: Vec<i32> = numbers.iter()
        .filter(|&&x| x % 2 == 0)
        .cloned()
        .collect();
    println!("Evens: {:?}", evens);

    let doubled: Vec<i32> = numbers.iter()
        .map(|&x| x * 2)
        .collect();
    println!("Doubled: {:?}", doubled);

    let sum: i32 = numbers.iter().sum();
    println!("Sum: {}", sum);
}
```

### 1.6 Functions as Parameters (Higher-Order Functions)

```rust
// ========== FUNCTION AS PARAMETER ==========
fn apply(f: fn(i32) -> i32, value: i32) -> i32 {
    f(value)
}

fn double(x: i32) -> i32 { x * 2 }
fn square(x: i32) -> i32 { x * x }

// ========== CLOSURE AS PARAMETER (using traits) ==========
fn apply_closure<F>(f: F, value: i32) -> i32
where
    F: Fn(i32) -> i32,     // Fn = immutable borrow
{
    f(value)
}

// ========== THREE CLOSURE TRAITS ==========
// Fn    → borrows captured values immutably
// FnMut → borrows captured values mutably
// FnOnce → takes ownership of captured values

fn do_twice<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
    f(x) + f(x)
}

fn mutate_and_call<F: FnMut()>(mut f: F) {
    f();
    f();
}

// ========== RETURNING CLOSURES ==========
fn make_adder(x: i32) -> Box<dyn Fn(i32) -> i32> {
    Box::new(move |y| x + y)
}

fn main() {
    // Pass regular functions
    println!("{}", apply(double, 5));     // 10
    println!("{}", apply(square, 5));     // 25

    // Pass closures
    println!("{}", apply_closure(|x| x + 10, 5));  // 15
    println!("{}", do_twice(|x| x * 3, 4));         // 24

    // Returned closure
    let add_five = make_adder(5);
    println!("{}", add_five(10));         // 15
    println!("{}", add_five(20));         // 25
}
```

### 1.7 Complete Function Reference

```
╔══════════════════════════════════════════════════════════════╗
║                  FUNCTION TYPES IN RUST                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Regular:    fn name(params) -> ReturnType { body }          ║
║  Method:     fn name(&self, params) -> ReturnType { body }   ║
║  Associated: fn name(params) -> ReturnType { body }  (no self)║
║  Generic:    fn name<T>(param: T) -> T { body }              ║
║  Closure:    let f = |params| body;                          ║
║  Async:      async fn name() -> ReturnType { body }          ║
║                                                              ║
║  PARAMETER PATTERNS:                                         ║
║  fn f(x: i32)          → takes ownership (copy for i32)     ║
║  fn f(s: String)       → takes ownership (move)             ║
║  fn f(s: &String)      → borrows immutably                  ║
║  fn f(s: &str)         → borrows string slice (preferred)   ║
║  fn f(s: &mut String)  → borrows mutably                    ║
║  fn f(s: &[i32])       → borrows slice                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## PART 2: "CLASSES" (Structs + Impl + Traits)

> Rust doesn't have classes. Instead it uses a composition of:
> **Struct** (data) + **Impl** (methods) + **Traits** (interfaces/behaviors)

### Comparison with OOP Languages
```
╔══════════════════╦══════════════════════════════════╗
║   OOP (C++/Java) ║         Rust Equivalent          ║
╠══════════════════╬══════════════════════════════════╣
║   class           ║  struct + impl                   ║
║   interface       ║  trait                           ║
║   inheritance     ║  trait + composition             ║
║   constructor     ║  associated function (::new())   ║
║   this/self       ║  &self, &mut self, self          ║
║   private field   ║  default (no pub)                ║
║   public field    ║  pub keyword                     ║
║   abstract class  ║  trait with default methods      ║
║   virtual method  ║  trait objects (dyn Trait)        ║
║   destructor      ║  Drop trait                      ║
║   operator overl. ║  std::ops traits                 ║
║   templates       ║  generics <T>                    ║
╚══════════════════╩══════════════════════════════════╝
```

### 2.1 Structs (Data Definition)

```rust
// ========== REGULAR STRUCT ==========
struct User {
    username: String,       // private by default
    email: String,
    age: u32,
    active: bool,
}

// ========== PUBLIC STRUCT (for use in other modules) ==========
pub struct Product {
    pub name: String,       // public field
    pub price: f64,         // public field
    sku: String,            // private field (even if struct is pub)
}

// ========== TUPLE STRUCT ==========
struct Color(u8, u8, u8);
struct Point2D(f64, f64);
struct Inches(f64);          // "newtype pattern" — wraps a single value

// ========== UNIT STRUCT (no fields) ==========
struct Marker;

// ========== GENERIC STRUCT ==========
struct Pair<T> {
    first: T,
    second: T,
}

struct KeyValue<K, V> {
    key: K,
    value: V,
}

fn main() {
    // Creating instances
    let user = User {
        username: String::from("alice"),
        email: String::from("alice@mail.com"),
        age: 30,
        active: true,
    };

    // Accessing fields
    println!("{} is {} years old", user.username, user.age);

    // Mutable struct
    let mut user2 = User {
        username: String::from("bob"),
        email: String::from("bob@mail.com"),
        age: 25,
        active: true,
    };
    user2.age = 26;   // modify field

    // Struct update syntax
    let user3 = User {
        username: String::from("charlie"),
        ..user2           // rest from user2 (user2 partially moved!)
    };

    // Tuple structs
    let red = Color(255, 0, 0);
    println!("R: {}, G: {}, B: {}", red.0, red.1, red.2);

    let origin = Point2D(0.0, 0.0);
    let height = Inches(72.0);

    // Generic structs
    let pair = Pair { first: 1, second: 2 };
    let kv = KeyValue { key: "name", value: "Alice" };
}
```

### 2.2 Impl Blocks (Methods & Associated Functions)

```rust
#[derive(Debug)]
struct Rectangle {
    width: f64,
    height: f64,
}

// ========== IMPL BLOCK — Methods and Associated Functions ==========
impl Rectangle {
    // ── ASSOCIATED FUNCTION (like static method / constructor) ──
    // Called with Rectangle::new()
    // No self parameter
    fn new(width: f64, height: f64) -> Rectangle {
        Rectangle { width, height }
    }

    fn square(size: f64) -> Rectangle {
        Rectangle { width: size, height: size }
    }

    // ── IMMUTABLE METHOD ──
    // Called with rect.area()
    // &self = immutable reference to instance
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    fn is_square(&self) -> bool {
        (self.width - self.height).abs() < f64::EPSILON
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    // ── MUTABLE METHOD ──
    // &mut self = mutable reference to instance
    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }

    fn set_width(&mut self, width: f64) {
        self.width = width;
    }

    // ── CONSUMING METHOD ──
    // self = takes ownership (instance can't be used after)
    fn into_square(self) -> Rectangle {
        let side = self.width.max(self.height);
        Rectangle { width: side, height: side }
    }
}

// You can have MULTIPLE impl blocks for the same struct
impl Rectangle {
    fn display(&self) {
        println!("Rectangle({}x{}) area={:.1}", 
            self.width, self.height, self.area());
    }
}

fn main() {
    // Associated functions (called with ::)
    let rect1 = Rectangle::new(10.0, 5.0);
    let rect2 = Rectangle::square(7.0);

    // Methods (called with .)
    println!("Area: {}", rect1.area());
    println!("Perimeter: {}", rect1.perimeter());
    println!("Is square? {}", rect1.is_square());
    println!("Can hold rect2? {}", rect1.can_hold(&rect2));
    rect1.display();

    // Mutable methods
    let mut rect3 = Rectangle::new(4.0, 3.0);
    rect3.scale(2.0);
    rect3.display();    // Rectangle(8x6)

    // Consuming method
    let rect4 = Rectangle::new(5.0, 3.0);
    let square = rect4.into_square();
    // rect4.area();    // ❌ ERROR: rect4 was consumed
    square.display();   // ✅ square is the new owner
}
```

### Self Parameter Reference
```
╔══════════════════════════════════════════════════════╗
║              SELF PARAMETER TYPES                    ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  &self      → borrows immutably (most common)       ║
║               can read but not modify                ║
║               instance usable after call             ║
║                                                      ║
║  &mut self  → borrows mutably                        ║
║               can read AND modify                    ║
║               instance usable after call             ║
║                                                      ║
║  self       → takes ownership (consumes)             ║
║               instance NOT usable after call         ║
║               used for transformations               ║
║                                                      ║
║  (no self)  → associated function (like static)      ║
║               called with Type::function()           ║
║               used for constructors                  ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

### 2.3 Traits (Interfaces / Behaviors)

```rust
// ========== DEFINING A TRAIT ==========
trait Shape {
    // Required methods (no body — must be implemented)
    fn area(&self) -> f64;
    fn perimeter(&self) -> f64;

    // Default method (has body — can be overridden)
    fn description(&self) -> String {
        format!("Shape with area {:.2}", self.area())
    }
}

trait Printable {
    fn print(&self);
}

// ========== STRUCTS ==========
struct Circle {
    radius: f64,
}

struct Rectangle {
    width: f64,
    height: f64,
}

struct Triangle {
    a: f64,
    b: f64,
    c: f64,
}

// ========== IMPLEMENTING TRAITS ==========
impl Shape for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }

    fn perimeter(&self) -> f64 {
        2.0 * std::f64::consts::PI * self.radius
    }

    // description() uses the default implementation
}

impl Shape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    // Override default method
    fn description(&self) -> String {
        format!("Rectangle {}x{} with area {:.2}", 
            self.width, self.height, self.area())
    }
}

impl Shape for Triangle {
    fn area(&self) -> f64 {
        // Heron's formula
        let s = (self.a + self.b + self.c) / 2.0;
        (s * (s - self.a) * (s - self.b) * (s - self.c)).sqrt()
    }

    fn perimeter(&self) -> f64 {
        self.a + self.b + self.c
    }
}

// Implement another trait
impl Printable for Circle {
    fn print(&self) {
        println!("Circle(radius={})", self.radius);
    }
}

impl Printable for Rectangle {
    fn print(&self) {
        println!("Rectangle({}x{})", self.width, self.height);
    }
}

// ========== USING TRAITS AS PARAMETERS ==========

// Option 1: impl Trait (static dispatch — fast)
fn print_area(shape: &impl Shape) {
    println!("Area: {:.2}", shape.area());
}

// Option 2: Trait bound syntax (same as above, more flexible)
fn print_info<T: Shape + Printable>(shape: &T) {
    shape.print();
    println!("  Area: {:.2}", shape.area());
    println!("  Perimeter: {:.2}", shape.perimeter());
}

// Option 3: Where clause (cleaner for complex bounds)
fn compare_areas<T, U>(shape1: &T, shape2: &U) -> String
where
    T: Shape,
    U: Shape,
{
    if shape1.area() > shape2.area() {
        String::from("First is larger")
    } else {
        String::from("Second is larger or equal")
    }
}

// Option 4: Trait objects (dynamic dispatch — flexible)
fn describe_all(shapes: &[&dyn Shape]) {
    for shape in shapes {
        println!("{}", shape.description());
    }
}

// ========== RETURNING TRAITS ==========
fn create_shape(kind: &str) -> Box<dyn Shape> {
    match kind {
        "circle" => Box::new(Circle { radius: 5.0 }),
        "rectangle" => Box::new(Rectangle { width: 4.0, height: 3.0 }),
        _ => Box::new(Circle { radius: 1.0 }),
    }
}

fn main() {
    let circle = Circle { radius: 5.0 };
    let rect = Rectangle { width: 10.0, height: 5.0 };
    let tri = Triangle { a: 3.0, b: 4.0, c: 5.0 };

    // Using trait methods
    print_area(&circle);
    print_area(&rect);
    print_area(&tri);

    // Multiple trait bounds
    print_info(&circle);
    print_info(&rect);

    // Comparing
    println!("{}", compare_areas(&circle, &rect));

    // Trait objects (heterogeneous collection)
    let shapes: Vec<&dyn Shape> = vec![&circle, &rect, &tri];
    describe_all(&shapes);

    // Dynamic creation
    let shape = create_shape("circle");
    println!("Dynamic: {}", shape.description());
}
```

### 2.4 Common Standard Library Traits

```rust
use std::fmt;

// ========== #[derive] — Auto-implement common traits ==========
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

// ========== Display (custom printing with {}) ==========
impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// ========== From / Into (type conversions) ==========
impl From<(i32, i32)> for Point {
    fn from(tuple: (i32, i32)) -> Self {
        Point { x: tuple.0, y: tuple.1 }
    }
}

// ========== Default (default values) ==========
impl Default for Point {
    fn default() -> Self {
        Point { x: 0, y: 0 }
    }
}

// Or with derive (if all fields implement Default):
#[derive(Debug, Default)]
struct Config {
    width: u32,      // defaults to 0
    height: u32,     // defaults to 0
    title: String,   // defaults to ""
    visible: bool,   // defaults to false
}

// ========== Drop (destructor) ==========
struct DatabaseConnection {
    name: String,
}

impl Drop for DatabaseConnection {
    fn drop(&mut self) {
        println!("Closing connection: {}", self.name);
    }
}

// ========== Iterator ==========
struct Counter {
    current: u32,
    max: u32,
}

impl Counter {
    fn new(max: u32) -> Counter {
        Counter { current: 0, max }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.current < self.max {
            self.current += 1;
            Some(self.current)
        } else {
            None
        }
    }
}

// ========== Operator Overloading ==========
use std::ops::{Add, Mul};

#[derive(Debug, Clone, Copy)]
struct Vector2D {
    x: f64,
    y: f64,
}

impl Add for Vector2D {
    type Output = Vector2D;
    fn add(self, other: Vector2D) -> Vector2D {
        Vector2D {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

impl Mul<f64> for Vector2D {
    type Output = Vector2D;
    fn mul(self, scalar: f64) -> Vector2D {
        Vector2D {
            x: self.x * scalar,
            y: self.y * scalar,
        }
    }
}

fn main() {
    // Display
    let p = Point { x: 3, y: 4 };
    println!("Display: {}", p);        // (3, 4)
    println!("Debug: {:?}", p);        // Point { x: 3, y: 4 }

    // Clone
    let p2 = p.clone();

    // PartialEq
    println!("Equal? {}", p == p2);    // true

    // From/Into
    let p3: Point = (5, 6).into();
    let p4 = Point::from((7, 8));
    println!("{}, {}", p3, p4);

    // Default
    let origin = Point::default();
    let config = Config::default();
    println!("Origin: {}", origin);

    // Partial default with struct update
    let custom_config = Config {
        width: 800,
        height: 600,
        ..Config::default()
    };

    // Drop
    {
        let conn = DatabaseConnection { name: String::from("main_db") };
        println!("Using connection...");
    }   // "Closing connection: main_db" printed here

    // Iterator
    let counter = Counter::new(5);
    for num in counter {
        print!("{} ", num);    // 1 2 3 4 5
    }
    println!();

    // Iterator methods work automatically!
    let sum: u32 = Counter::new(10).sum();
    println!("Sum 1-10: {}", sum);

    let evens: Vec<u32> = Counter::new(10)
        .filter(|x| x % 2 == 0)
        .collect();
    println!("Evens: {:?}", evens);

    // Operator overloading
    let v1 = Vector2D { x: 1.0, y: 2.0 };
    let v2 = Vector2D { x: 3.0, y: 4.0 };
    let v3 = v1 + v2;
    let v4 = v1 * 3.0;
    println!("v1 + v2 = {:?}", v3);
    println!("v1 * 3 = {:?}", v4);
}
```

### Derivable Traits Cheat Sheet
```
╔══════════════╦═══════════════════════════════════════╗
║  Trait        ║  What it does                         ║
╠══════════════╬═══════════════════════════════════════╣
║  Debug        ║  Enable {:?} printing                 ║
║  Clone        ║  Enable .clone() deep copy            ║
║  Copy         ║  Implicit copy (stack types only)     ║
║  PartialEq    ║  Enable == and != comparison          ║
║  Eq           ║  Full equality (no NaN issues)        ║
║  PartialOrd   ║  Enable <, >, <=, >= comparison       ║
║  Ord          ║  Full ordering (for sorting)          ║
║  Hash         ║  Enable use as HashMap key            ║
║  Default      ║  Enable Type::default()               ║
╚══════════════╩═══════════════════════════════════════╝

Usage:
  #[derive(Debug, Clone, PartialEq, Default)]
  struct MyStruct { ... }
```

### 2.5 Trait Inheritance & Supertraits

```rust
trait Animal {
    fn name(&self) -> &str;
    fn sound(&self) -> &str;
}

// Pet REQUIRES Animal to be implemented first
trait Pet: Animal {
    fn cuddle(&self) {
        println!("{} loves cuddles!", self.name());
    }
}

trait Trainable: Pet {
    fn train(&self, command: &str) {
        println!("Training {} to: {}", self.name(), command);
    }
}

struct Dog {
    name: String,
    breed: String,
}

impl Animal for Dog {
    fn name(&self) -> &str { &self.name }
    fn sound(&self) -> &str { "Woof!" }
}

impl Pet for Dog {}          // uses default cuddle()
impl Trainable for Dog {}    // uses default train()

fn main() {
    let dog = Dog {
        name: String::from("Rex"),
        breed: String::from("Labrador"),
    };
    println!("{} says {}", dog.name(), dog.sound());
    dog.cuddle();
    dog.train("sit");
}
```

### 2.6 Full "Class-like" Example

```rust
use std::fmt;

// ========== "CLASS" = Struct + Impl + Traits ==========

#[derive(Debug, Clone)]
pub struct BankAccount {
    owner: String,
    account_number: String,
    balance: f64,
    is_active: bool,
    transactions: Vec<Transaction>,
}

#[derive(Debug, Clone)]
struct Transaction {
    kind: TransactionType,
    amount: f64,
    description: String,
}

#[derive(Debug, Clone)]
enum TransactionType {
    Deposit,
    Withdrawal,
}

// ── Methods ──
impl BankAccount {
    // Constructor
    pub fn new(owner: &str, account_number: &str) -> Self {
        BankAccount {
            owner: String::from(owner),
            account_number: String::from(account_number),
            balance: 0.0,
            is_active: true,
            transactions: Vec::new(),
        }
    }

    // Constructor with initial deposit
    pub fn with_balance(owner: &str, account_number: &str, initial: f64) -> Self {
        let mut account = Self::new(owner, account_number);
        if initial > 0.0 {
            account.balance = initial;
            account.transactions.push(Transaction {
                kind: TransactionType::Deposit,
                amount: initial,
                description: String::from("Initial deposit"),
            });
        }
        account
    }

    // Getters
    pub fn owner(&self) -> &str { &self.owner }
    pub fn balance(&self) -> f64 { self.balance }
    pub fn is_active(&self) -> bool { self.is_active }

    // Methods
    pub fn deposit(&mut self, amount: f64, description: &str) -> Result<f64, String> {
        if !self.is_active {
            return Err(String::from("Account is inactive"));
        }
        if amount <= 0.0 {
            return Err(String::from("Amount must be positive"));
        }

        self.balance += amount;
        self.transactions.push(Transaction {
            kind: TransactionType::Deposit,
            amount,
            description: String::from(description),
        });
        Ok(self.balance)
    }

    pub fn withdraw(&mut self, amount: f64, description: &str) -> Result<f64, String> {
        if !self.is_active {
            return Err(String::from("Account is inactive"));
        }
        if amount <= 0.0 {
            return Err(String::from("Amount must be positive"));
        }
        if amount > self.balance {
            return Err(format!("Insufficient funds. Balance: {:.2}", self.balance));
        }

        self.balance -= amount;
        self.transactions.push(Transaction {
            kind: TransactionType::Withdrawal,
            amount,
            description: String::from(description),
        });
        Ok(self.balance)
    }

    pub fn transfer(&mut self, other: &mut BankAccount, amount: f64) -> Result<(), String> {
        self.withdraw(amount, &format!("Transfer to {}", other.owner))?;
        other.deposit(amount, &format!("Transfer from {}", self.owner))?;
        Ok(())
    }

    pub fn deactivate(&mut self) {
        self.is_active = false;
    }

    pub fn transaction_count(&self) -> usize {
        self.transactions.len()
    }

    pub fn print_statement(&self) {
        println!("\n=== Account Statement ===");
        println!("Owner: {}", self.owner);
        println!("Account: {}", self.account_number);
        println!("Status: {}", if self.is_active { "Active" } else { "Inactive" });
        println!("─────────────────────────");
        for (i, t) in self.transactions.iter().enumerate() {
            let sign = match t.kind {
                TransactionType::Deposit => "+",
                TransactionType::Withdrawal => "-",
            };
            println!("  {}. {}{:.2} — {}", i + 1, sign, t.amount, t.description);
        }
        println!("─────────────────────────");
        println!("Balance: ${:.2}\n", self.balance);
    }
}

// ── Display Trait ──
impl fmt::Display for BankAccount {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "BankAccount({}, ${:.2})", self.owner, self.balance)
    }
}

// ── PartialEq (compare by account number) ──
impl PartialEq for BankAccount {
    fn eq(&self, other: &Self) -> bool {
        self.account_number == other.account_number
    }
}

fn main() {
    let mut alice = BankAccount::with_balance("Alice", "ACC-001", 1000.0);
    let mut bob = BankAccount::new("Bob", "ACC-002");

    println!("{}", alice);    // BankAccount(Alice, $1000.00)
    println!("{}", bob);      // BankAccount(Bob, $0.00)

    // Deposits
    alice.deposit(500.0, "Salary").unwrap();
    bob.deposit(200.0, "Gift").unwrap();

    // Withdrawal
    match alice.withdraw(10000.0, "Shopping") {
        Ok(balance) => println!("New balance: {:.2}", balance),
        Err(e) => println!("Error: {}", e),
    }

    alice.withdraw(300.0, "Groceries").unwrap();

    // Transfer
    alice.transfer(&mut bob, 250.0).unwrap();

    // Statements
    alice.print_statement();
    bob.print_statement();

    // Comparison
    println!("Same account? {}", alice == bob);   // false
}
```

---

## PART 3: DATA STRUCTURES

### 3.1 Built-in Data Structures Overview

```
╔══════════════════════════════════════════════════════════════╗
║              RUST DATA STRUCTURES                            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  SEQUENCES (ordered)                                         ║
║  ├── Array        [T; N]       Fixed size, stack             ║
║  ├── Vec<T>       Vec::new()   Dynamic array, heap           ║
║  ├── VecDeque<T>               Double-ended queue            ║
║  └── LinkedList<T>             Doubly-linked list            ║
║                                                              ║
║  MAPS (key-value)                                            ║
║  ├── HashMap<K,V>              Hash table (unordered)        ║
║  └── BTreeMap<K,V>             Sorted tree map               ║
║                                                              ║
║  SETS (unique values)                                        ║
║  ├── HashSet<T>                Hash set (unordered)          ║
║  └── BTreeSet<T>               Sorted tree set               ║
║                                                              ║
║  STRINGS                                                     ║
║  ├── String                    Owned, growable, heap          ║
║  └── &str                      Borrowed string slice          ║
║                                                              ║
║  SMART POINTERS                                              ║
║  ├── Box<T>                    Heap allocation                ║
║  ├── Rc<T>                     Reference counting             ║
║  ├── Arc<T>                    Atomic ref counting (threads)  ║
║  ├── RefCell<T>                Interior mutability            ║
║  └── Mutex<T>                  Thread-safe interior mut       ║
║                                                              ║
║  OTHER                                                       ║
║  ├── Option<T>                 Some(T) or None                ║
║  ├── Result<T,E>               Ok(T) or Err(E)               ║
║  ├── Tuple        (T, U, V)   Fixed heterogeneous            ║
║  └── Slice         &[T]        View into contiguous data      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### 3.2 Array (Fixed-Size)

```rust
fn main() {
    // ========== CREATION ==========
    let arr: [i32; 5] = [1, 2, 3, 4, 5];      // explicit type
    let arr2 = [1, 2, 3, 4, 5];                // type inferred
    let zeros = [0; 10];                        // [0, 0, 0, ..., 0]
    let names = ["Alice", "Bob", "Charlie"];

    // ========== ACCESS ==========
    println!("First: {}", arr[0]);
    println!("Last: {}", arr[arr.len() - 1]);

    // Safe access
    match arr.get(10) {
        Some(val) => println!("Got: {}", val),
        None => println!("Index out of bounds"),
    }

    // ========== ITERATION ==========
    for val in &arr {
        print!("{} ", val);
    }
    println!();

    for (i, val) in arr.iter().enumerate() {
        println!("[{}] = {}", i, val);
    }

    // ========== USEFUL METHODS ==========
    println!("Length: {}", arr.len());
    println!("Contains 3? {}", arr.contains(&3));
    println!("Is empty? {}", arr.is_empty());

    // Slicing
    let slice = &arr[1..4];          // [2, 3, 4]
    println!("Slice: {:?}", slice);

    // Sorting (need mutable)
    let mut nums = [5, 2, 8, 1, 9];
    nums.sort();
    println!("Sorted: {:?}", nums);

    // Map/Filter (via iterators)
    let doubled: Vec<i32> = arr.iter().map(|&x| x * 2).collect();
    println!("Doubled: {:?}", doubled);

    // ========== MULTIDIMENSIONAL ==========
    let matrix: [[i32; 3]; 3] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ];
    println!("Center: {}", matrix[1][1]);   // 5

    for row in &matrix {
        for val in row {
            print!("{:3}", val);
        }
        println!();
    }
}
```

### 3.3 Vec<T> (Dynamic Array — Most Used!)

```rust
fn main() {
    // ========== CREATION ==========
    let mut v1: Vec<i32> = Vec::new();
    let v2 = vec![1, 2, 3, 4, 5];
    let v3 = vec![0; 10];                    // 10 zeros
    let v4: Vec<i32> = (1..=10).collect();   // from range
    let v5 = Vec::with_capacity(100);        // pre-allocate

    // ========== ADDING ELEMENTS ==========
    let mut v = Vec::new();
    v.push(1);                     // add to end
    v.push(2);
    v.push(3);
    v.insert(1, 99);              // insert at index → [1, 99, 2, 3]
    v.extend([10, 20, 30]);       // add multiple
    v.append(&mut vec![40, 50]);  // move all from another vec
    println!("{:?}", v);

    // ========== REMOVING ELEMENTS ==========
    let last = v.pop();           // remove last → Option<T>
    v.remove(0);                  // remove at index
    v.retain(|&x| x > 5);        // keep only elements > 5
    v.dedup();                    // remove consecutive duplicates
    // v.clear();                 // remove all

    // ========== ACCESSING ==========
    let nums = vec![10, 20, 30, 40, 50];

    let first = nums[0];                    // panics if out of bounds
    let safe = nums.get(0);                 // Option<&T>
    let first_ref = nums.first();           // Option<&T>
    let last_ref = nums.last();             // Option<&T>

    println!("First: {}", first);
    println!("Safe: {:?}", safe);

    // ========== SLICING ==========
    let slice = &nums[1..4];                // &[20, 30, 40]
    println!("Slice: {:?}", slice);

    // ========== ITERATION ==========
    // Immutable
    for val in &nums {
        print!("{} ", val);
    }
    println!();

    // Mutable
    let mut nums = vec![1, 2, 3, 4, 5];
    for val in &mut nums {
        *val *= 10;
    }
    println!("{:?}", nums);   // [10, 20, 30, 40, 50]

    // With index
    for (i, val) in nums.iter().enumerate() {
        println!("[{}] = {}", i, val);
    }

    // ========== SEARCHING ==========
    let data = vec![3, 1, 4, 1, 5, 9, 2, 6];

    println!("Contains 5? {}", data.contains(&5));
    println!("Position of 4: {:?}", data.iter().position(|&x| x == 4));
    println!("Find first >5: {:?}", data.iter().find(|&&x| x > 5));

    // ========== SORTING ==========
    let mut nums = vec![3, 1, 4, 1, 5, 9, 2, 6];
    nums.sort();                             // ascending
    println!("Sorted: {:?}", nums);

    nums.sort_by(|a, b| b.cmp(a));          // descending
    println!("Descending: {:?}", nums);

    // Sort floats
    let mut floats = vec![3.1, 1.4, 2.7, 0.5];
    floats.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!("Floats sorted: {:?}", floats);

    // ========== ITERATOR METHODS (very powerful!) ==========
    let data = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // Map
    let squares: Vec<i32> = data.iter().map(|&x| x * x).collect();

    // Filter
    let evens: Vec<&i32> = data.iter().filter(|&&x| x % 2 == 0).collect();

    // Filter + Map combined
    let even_squares: Vec<i32> = data.iter()
        .filter(|&&x| x % 2 == 0)
        .map(|&x| x * x)
        .collect();

    // Reduce/Fold
    let sum: i32 = data.iter().sum();
    let product: i32 = data.iter().product();
    let max = data.iter().max();
    let min = data.iter().min();

    // Any / All
    let has_even = data.iter().any(|&x| x % 2 == 0);
    let all_positive = data.iter().all(|&x| x > 0);

    // Take / Skip
    let first_3: Vec<&i32> = data.iter().take(3).collect();
    let skip_3: Vec<&i32> = data.iter().skip(3).collect();

    // Chain
    let a = vec![1, 2];
    let b = vec![3, 4];
    let combined: Vec<&i32> = a.iter().chain(b.iter()).collect();

    // Zip
    let names = vec!["Alice", "Bob"];
    let ages = vec![25, 30];
    let pairs: Vec<(&&str, &i32)> = names.iter().zip(ages.iter()).collect();

    // Flat map
    let nested = vec![vec![1, 2], vec![3, 4], vec![5, 6]];
    let flat: Vec<&i32> = nested.iter().flat_map(|v| v.iter()).collect();

    println!("Squares: {:?}", squares);
    println!("Evens: {:?}", evens);
    println!("Even squares: {:?}", even_squares);
    println!("Sum: {}, Product: {}", sum, product);
    println!("Max: {:?}, Min: {:?}", max, min);
    println!("Pairs: {:?}", pairs);
    println!("Flat: {:?}", flat);

    // ========== INFO ==========
    let v = vec![1, 2, 3, 4, 5];
    println!("Length: {}", v.len());
    println!("Capacity: {}", v.capacity());
    println!("Is empty? {}", v.is_empty());
}
```

### 3.4 HashMap<K, V>

```rust
use std::collections::HashMap;

fn main() {
    // ========== CREATION ==========
    let mut map: HashMap<String, i32> = HashMap::new();
    let mut scores = HashMap::new();       // type inferred on insert

    // From arrays/tuples
    let solar: HashMap<&str, i32> = HashMap::from([
        ("Mercury", 1),
        ("Venus", 2),
        ("Earth", 3),
    ]);

    // From iterators
    let names = vec!["Alice", "Bob"];
    let ages = vec![25, 30];
    let people: HashMap<_, _> = names.into_iter().zip(ages.into_iter()).collect();

    // ========== INSERTING ==========
    scores.insert(String::from("Alice"), 95);
    scores.insert(String::from("Bob"), 87);
    scores.insert(String::from("Charlie"), 92);

    // Insert only if key doesn't exist
    scores.entry(String::from("Dave")).or_insert(80);
    scores.entry(String::from("Alice")).or_insert(0);  // won't overwrite

    // Insert with computation
    scores.entry(String::from("Eve")).or_insert_with(|| {
        // expensive computation
        88
    });

    // ========== ACCESSING ==========
    // Direct (panics if missing)
    // let alice = scores["Alice"];    // works but dangerous

    // Safe access
    match scores.get("Alice") {
        Some(score) => println!("Alice: {}", score),
        None => println!("Alice not found"),
    }

    // With default
    let score = scores.get("Unknown").unwrap_or(&0);
    println!("Unknown: {}", score);

    // ========== MODIFYING ==========
    // Overwrite
    scores.insert(String::from("Alice"), 100);

    // Modify existing value
    if let Some(score) = scores.get_mut("Bob") {
        *score += 10;
    }

    // Update based on old value (word counting pattern)
    let text = "hello world hello rust hello world";
    let mut word_count: HashMap<&str, i32> = HashMap::new();
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);
        *count += 1;
    }
    println!("Word count: {:?}", word_count);

    // ========== REMOVING ==========
    scores.remove("Charlie");
    // Remove and get value
    if let Some(removed) = scores.remove("Bob") {
        println!("Removed Bob with score {}", removed);
    }

    // ========== ITERATION ==========
    for (name, score) in &scores {
        println!("{}: {}", name, score);
    }

    // Keys only
    let names: Vec<&String> = scores.keys().collect();
    
    // Values only
    let all_scores: Vec<&i32> = scores.values().collect();

    // ========== CHECKING ==========
    println!("Contains Alice? {}", scores.contains_key("Alice"));
    println!("Length: {}", scores.len());
    println!("Is empty? {}", scores.is_empty());

    // ========== COMPLEX VALUES ==========
    #[derive(Debug)]
    struct Student {
        name: String,
        grades: Vec<i32>,
    }

    let mut students: HashMap<String, Student> = HashMap::new();
    students.insert(
        String::from("S001"),
        Student {
            name: String::from("Alice"),
            grades: vec![90, 85, 92],
        },
    );

    if let Some(student) = students.get("S001") {
        println!("{:?}", student);
    }
}
```

### 3.5 HashSet<T>

```rust
use std::collections::HashSet;

fn main() {
    // ========== CREATION ==========
    let mut set: HashSet<i32> = HashSet::new();
    let primes: HashSet<i32> = HashSet::from([2, 3, 5, 7, 11]);
    let from_vec: HashSet<i32> = vec![1, 2, 2, 3, 3, 3].into_iter().collect();
    println!("Unique: {:?}", from_vec);   // {1, 2, 3}

    // ========== ADDING ==========
    set.insert(1);
    set.insert(2);
    set.insert(3);
    let was_new = set.insert(4);      // returns true (new element)
    let was_dup = set.insert(2);      // returns false (already exists)

    // ========== REMOVING ==========
    set.remove(&3);
    // set.clear();

    // ========== CHECKING ==========
    println!("Contains 2? {}", set.contains(&2));
    println!("Length: {}", set.len());

    // ========== SET OPERATIONS ==========
    let a: HashSet<i32> = [1, 2, 3, 4, 5].into();
    let b: HashSet<i32> = [3, 4, 5, 6, 7].into();

    // Union (all elements from both)
    let union: HashSet<&i32> = a.union(&b).collect();
    println!("Union: {:?}", union);

    // Intersection (common elements)
    let inter: HashSet<&i32> = a.intersection(&b).collect();
    println!("Intersection: {:?}", inter);

    // Difference (in a but not in b)
    let diff: HashSet<&i32> = a.difference(&b).collect();
    println!("A - B: {:?}", diff);

    // Symmetric difference (in one but not both)
    let sym_diff: HashSet<&i32> = a.symmetric_difference(&b).collect();
    println!("Symmetric diff: {:?}", sym_diff);

    // Subset / Superset
    let small: HashSet<i32> = [1, 2].into();
    println!("small ⊂ a? {}", small.is_subset(&a));
    println!("a ⊃ small? {}", a.is_superset(&small));

    // Disjoint (no common elements)
    let x: HashSet<i32> = [1, 2].into();
    let y: HashSet<i32> = [3, 4].into();
    println!("Disjoint? {}", x.is_disjoint(&y));
}
```

### 3.6 VecDeque (Double-Ended Queue)

```rust
use std::collections::VecDeque;

fn main() {
    let mut deque: VecDeque<i32> = VecDeque::new();

    // Add to front and back
    deque.push_back(1);        // [1]
    deque.push_back(2);        // [1, 2]
    deque.push_front(0);       // [0, 1, 2]
    deque.push_front(-1);      // [-1, 0, 1, 2]

    println!("{:?}", deque);

    // Remove from front and back
    let front = deque.pop_front();    // Some(-1)
    let back = deque.pop_back();      // Some(2)
    println!("Front: {:?}, Back: {:?}", front, back);

    // Access
    println!("First: {:?}", deque.front());
    println!("Last: {:?}", deque.back());
    println!("Index 1: {}", deque[1]);

    // Use as queue (FIFO)
    let mut queue: VecDeque<&str> = VecDeque::new();
    queue.push_back("first");
    queue.push_back("second");
    queue.push_back("third");
    while let Some(item) = queue.pop_front() {
        println!("Processing: {}", item);
    }

    // Use as stack (LIFO)
    let mut stack: VecDeque<i32> = VecDeque::new();
    stack.push_back(1);
    stack.push_back(2);
    stack.push_back(3);
    while let Some(item) = stack.pop_back() {
        println!("Popped: {}", item);
    }
}
```

### 3.7 BTreeMap & BTreeSet (Sorted Collections)

```rust
use std::collections::{BTreeMap, BTreeSet};

fn main() {
    // ========== BTreeMap (sorted by key) ==========
    let mut map = BTreeMap::new();
    map.insert("Charlie", 92);
    map.insert("Alice", 95);
    map.insert("Bob", 87);

    // Always iterated in sorted key order!
    for (name, score) in &map {
        println!("{}: {}", name, score);
    }
    // Alice: 95
    // Bob: 87
    // Charlie: 92

    // Range queries
    for (name, score) in map.range("A"..="B") {
        println!("Range: {}: {}", name, score);
    }

    // ========== BTreeSet (sorted unique values) ==========
    let mut set = BTreeSet::new();
    set.insert(5);
    set.insert(2);
    set.insert(8);
    set.insert(1);
    set.insert(9);

    // Always in sorted order!
    println!("{:?}", set);    // {1, 2, 5, 8, 9}

    // Range
    let range: Vec<&i32> = set.range(2..=8).collect();
    println!("2..=8: {:?}", range);   // [2, 5, 8]
}
```

### 3.8 Smart Pointers

```rust
use std::rc::Rc;
use std::cell::RefCell;

fn main() {
    // ========== Box<T> — Heap Allocation ==========
    // Use when:
    // - Type size unknown at compile time
    // - Large data you don't want to copy
    // - Recursive types

    let boxed = Box::new(42);
    println!("Boxed: {}", boxed);      // auto-dereferenced

    // Recursive type (impossible without Box)
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }

    let list = List::Cons(1,
        Box::new(List::Cons(2,
            Box::new(List::Cons(3,
                Box::new(List::Nil))))));
    println!("{:?}", list);

    // ========== Rc<T> — Reference Counting ==========
    // Use when: multiple owners needed (single-threaded)

    let shared = Rc::new(String::from("shared data"));
    let clone1 = Rc::clone(&shared);    // cheap clone (just increments counter)
    let clone2 = Rc::clone(&shared);

    println!("References: {}", Rc::strong_count(&shared));  // 3
    println!("Data: {}", shared);
    println!("Same data: {}", clone1);

    drop(clone1);
    println!("After drop: {}", Rc::strong_count(&shared));  // 2

    // ========== RefCell<T> — Interior Mutability ==========
    // Use when: need to mutate data behind immutable reference

    let data = RefCell::new(vec![1, 2, 3]);

    // Borrow mutably at runtime (checked at runtime, not compile time)
    data.borrow_mut().push(4);
    data.borrow_mut().push(5);

    println!("Data: {:?}", data.borrow());   // [1, 2, 3, 4, 5]

    // ========== Rc<RefCell<T>> — Shared Mutable Data ==========
    let shared_vec = Rc::new(RefCell::new(vec![1, 2, 3]));

    let owner1 = Rc::clone(&shared_vec);
    let owner2 = Rc::clone(&shared_vec);

    owner1.borrow_mut().push(4);
    owner2.borrow_mut().push(5);

    println!("Shared: {:?}", shared_vec.borrow());  // [1, 2, 3, 4, 5]
}
```

### 3.9 Option<T> & Result<T, E>

```rust
fn main() {
    // ========== Option<T> — Value that might not exist ==========
    // enum Option<T> {
    //     Some(T),
    //     None,
    // }

    let some_val: Option<i32> = Some(42);
    let no_val: Option<i32> = None;

    // Pattern matching
    match some_val {
        Some(v) => println!("Got: {}", v),
        None => println!("Nothing"),
    }

    // if let
    if let Some(v) = some_val {
        println!("Value: {}", v);
    }

    // Methods
    println!("{}", some_val.unwrap());            // 42 (panics on None!)
    println!("{}", no_val.unwrap_or(0));          // 0 (safe default)
    println!("{}", no_val.unwrap_or_default());   // 0 (type's default)
    println!("{}", some_val.is_some());           // true
    println!("{}", no_val.is_none());             // true

    // Map (transform the inner value)
    let doubled = some_val.map(|v| v * 2);       // Some(84)
    let none_doubled = no_val.map(|v| v * 2);    // None

    // And then (chain operations that return Option)
    let result = some_val
        .map(|v| v * 2)
        .filter(


# 🦀 Rust Architecture, Structure, Libraries & External Communication

---

## PART 1: OVERALL ARCHITECTURE OF RUST

### 1.1 The Big Picture

```
╔═══════════════════════════════════════════════════════════════════╗
║                    RUST ARCHITECTURE OVERVIEW                     ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  YOUR CODE (.rs files)                                            ║
║       │                                                           ║
║       ▼                                                           ║
║  ┌─────────────────────────────────────────────┐                  ║
║  │            RUST COMPILER (rustc)            │                  ║
║  │                                             │                  ║
║  │  1. Lexing/Parsing → AST                    │                  ║
║  │  2. Name Resolution                         │                  ║
║  │  3. Macro Expansion                         │                  ║
║  │  4. HIR (High-Level IR)                     │                  ║
║  │  5. Type Checking + Borrow Checker ⭐        │                  ║
║  │  6. MIR (Mid-Level IR)                      │                  ║
║  │  7. Optimization                            │                  ║
║  │  8. LLVM IR Generation                      │                  ║
║  └──────────────┬──────────────────────────────┘                  ║
║                 │                                                  ║
║                 ▼                                                  ║
║  ┌─────────────────────────────────────────────┐                  ║
║  │              LLVM Backend                   │                  ║
║  │  • Optimization passes                      │                  ║
║  │  • Machine code generation                  │                  ║
║  │  • Platform-specific output                 │                  ║
║  └──────────────┬──────────────────────────────┘                  ║
║                 │                                                  ║
║                 ▼                                                  ║
║  ┌─────────────────────────────────────────────┐                  ║
║  │         NATIVE BINARY / LIBRARY             │                  ║
║  │  • Executable (.exe / ELF)                  │                  ║
║  │  • Static library (.a / .lib)               │                  ║
║  │  • Dynamic library (.so / .dll / .dylib)    │                  ║
║  │  • WebAssembly (.wasm)                      │                  ║
║  └─────────────────────────────────────────────┘                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 1.2 Compiler Pipeline (Detailed)

```
Source Code (.rs)
    │
    ▼
┌──────────────────────┐
│  1. LEXER/TOKENIZER  │  Breaks code into tokens
│     "let x = 5;"     │  → [LET, IDENT("x"), EQ, INT(5), SEMI]
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  2. PARSER           │  Builds Abstract Syntax Tree (AST)
│     Tokens → AST     │  Checks syntax correctness
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  3. MACRO EXPANSION  │  Expands println!, vec!, derive, etc.
│     AST → AST        │  Procedural & declarative macros
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  4. HIR (High IR)    │  Desugared Rust
│     AST → HIR        │  for loops → loop + match
│                      │  if let → match
│                      │  ? operator → match Result
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  5. TYPE CHECKING     │  ⭐ Rust's signature feature
│  + BORROW CHECKER     │  • Ownership verification
│     HIR → THIR       │  • Lifetime validation
│                      │  • Type inference
│                      │  • Trait resolution
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  6. MIR (Mid IR)     │  Simplified control flow
│     THIR → MIR       │  • Borrow checking (again, deeper)
│                      │  • Optimization
│                      │  • Monomorphization (generics → concrete)
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  7. LLVM IR          │  Platform-independent low-level code
│     MIR → LLVM IR    │  Handed to LLVM for optimization
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  8. LLVM BACKEND     │  Machine code generation
│     LLVM IR → Binary │  Platform-specific optimizations
└──────────┬───────────┘
           ▼
    Native Binary
```

### 1.3 Rust Toolchain

```
╔════════════════════════════════════════════════════════════════╗
║                    RUST TOOLCHAIN                              ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  rustup (Toolchain Manager)                                    ║
║  ├── Manages Rust installations                                ║
║  ├── Switches between stable/beta/nightly                      ║
║  ├── Manages cross-compilation targets                         ║
║  └── Updates components                                        ║
║                                                                ║
║  rustc (Compiler)                                              ║
║  ├── Compiles .rs files to binary                              ║
║  ├── Type checking + borrow checking                           ║
║  └── Usually invoked through cargo                             ║
║                                                                ║
║  cargo (Build System + Package Manager)                        ║
║  ├── Creates projects                                          ║
║  ├── Manages dependencies (from crates.io)                     ║
║  ├── Builds, tests, runs, benchmarks                           ║
║  ├── Publishes crates                                          ║
║  └── Manages workspaces                                        ║
║                                                                ║
║  clippy (Linter)                                               ║
║  ├── Catches common mistakes                                   ║
║  ├── Suggests idiomatic code                                   ║
║  └── cargo clippy                                              ║
║                                                                ║
║  rustfmt (Formatter)                                           ║
║  ├── Auto-formats code to standard style                       ║
║  └── cargo fmt                                                 ║
║                                                                ║
║  rust-analyzer (IDE Support)                                   ║
║  ├── Code completion                                           ║
║  ├── Go to definition                                          ║
║  ├── Inline errors                                             ║
║  └── Refactoring                                               ║
║                                                                ║
║  rustdoc (Documentation Generator)                             ║
║  ├── Generates HTML docs from /// comments                     ║
║  └── cargo doc                                                 ║
║                                                                ║
║  miri (Interpreter)                                            ║
║  ├── Detects undefined behavior                                ║
║  └── Tests unsafe code                                         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

```bash
# Toolchain commands
rustup show                    # Show installed toolchains
rustup update                  # Update Rust
rustup default stable          # Use stable
rustup default nightly         # Use nightly
rustup target add wasm32-unknown-unknown  # Add WASM target
rustup component add clippy rustfmt       # Add components

# Compiler
rustc --version                # Version
rustc main.rs                  # Compile single file
rustc --edition 2021 main.rs   # Specify edition

# Cargo (you'll use this 99% of the time)
cargo new my_project           # Create new project
cargo build                    # Compile
cargo build --release          # Compile optimized
cargo run                      # Compile and run
cargo test                     # Run tests
cargo bench                    # Run benchmarks
cargo doc --open               # Generate and open docs
cargo clippy                   # Run linter
cargo fmt                      # Format code
cargo check                    # Fast error checking
cargo update                   # Update dependencies
cargo publish                  # Publish to crates.io
cargo install tool_name        # Install binary crate
```

### 1.4 Compilation Targets

```
╔════════════════════════════════════════════════════════════╗
║                 RUST COMPILATION TARGETS                   ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  NATIVE PLATFORMS                                          ║
║  ├── x86_64-unknown-linux-gnu     (Linux 64-bit)          ║
║  ├── x86_64-apple-darwin          (macOS 64-bit)          ║
║  ├── x86_64-pc-windows-msvc      (Windows 64-bit)        ║
║  ├── aarch64-unknown-linux-gnu    (Linux ARM64)           ║
║  ├── aarch64-apple-darwin         (macOS M1/M2)           ║
║  └── ... 80+ supported targets                            ║
║                                                            ║
║  EMBEDDED                                                  ║
║  ├── thumbv7em-none-eabihf       (ARM Cortex-M)          ║
║  ├── riscv32imac-unknown-none-elf (RISC-V)               ║
║  └── Various microcontrollers                              ║
║                                                            ║
║  WEB                                                       ║
║  ├── wasm32-unknown-unknown       (WebAssembly)           ║
║  └── wasm32-wasi                  (WASM + System Interface)║
║                                                            ║
║  CROSS-COMPILATION                                         ║
║  └── Compile on one platform, run on another               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

### 1.5 Memory Architecture

```
╔═════════════════════════════════════════════════════════════╗
║              RUST MEMORY MODEL                              ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║  ┌─────────────────────────────────────┐                    ║
║  │           STACK                      │                   ║
║  │  • Fixed-size data                   │  Fast             ║
║  │  • Function frames                   │  Auto-managed     ║
║  │  • Local variables                   │  LIFO order       ║
║  │  • References (&T)                   │                   ║
║  │  • Primitives (i32, f64, bool)       │                   ║
║  │  • Fixed arrays [T; N]               │                   ║
║  │  • Tuples                            │                   ║
║  └─────────────────────────────────────┘                    ║
║                                                             ║
║  ┌─────────────────────────────────────┐                    ║
║  │            HEAP                      │                   ║
║  │  • Dynamic-size data                 │  Slower           ║
║  │  • Owned by stack variables          │  Manual via       ║
║  │  • String contents                   │  ownership        ║
║  │  • Vec<T> contents                   │                   ║
║  │  • Box<T> contents                   │  No GC!           ║
║  │  • HashMap contents                  │  No malloc/free!  ║
║  └─────────────────────────────────────┘                    ║
║                                                             ║
║  ┌─────────────────────────────────────┐                    ║
║  │        STATIC / GLOBAL              │                    ║
║  │  • String literals ("hello")         │  Lives forever    ║
║  │  • static variables                  │  Program lifetime ║
║  │  • const values                      │                   ║
║  │  • Program binary                    │                   ║
║  └─────────────────────────────────────┘                    ║
║                                                             ║
║  KEY PRINCIPLE: No garbage collector!                       ║
║  Memory is freed when the OWNER goes out of scope.          ║
║  The compiler inserts drop() calls at compile time.         ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
```

```rust
fn main() {
    // STACK allocated
    let x: i32 = 42;                    // stack
    let arr: [i32; 5] = [1, 2, 3, 4, 5]; // stack
    let tuple: (i32, f64) = (1, 2.0);   // stack
    let reference: &str = "hello";       // pointer on stack, data in static

    // HEAP allocated (owned by stack variable)
    let string: String = String::from("hello");  // metadata on stack, data on heap
    let vector: Vec<i32> = vec![1, 2, 3];        // metadata on stack, data on heap
    let boxed: Box<i32> = Box::new(42);           // pointer on stack, data on heap

    // When this function ends:
    // - Stack variables are popped automatically
    // - Heap data is freed via Drop trait (no GC needed!)
}
```

---

## PART 2: HOW RUST CODE IS STRUCTURED

### 2.1 Project Hierarchy

```
╔═══════════════════════════════════════════════════════════╗
║                RUST CODE ORGANIZATION                     ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ECOSYSTEM                                                ║
║  └── crates.io (package registry — like npm/PyPI)         ║
║                                                           ║
║  WORKSPACE (optional — multi-package project)             ║
║  └── Contains multiple packages                           ║
║                                                           ║
║  PACKAGE (a Cargo.toml file)                              ║
║  └── Contains one or more crates                          ║
║                                                           ║
║  CRATE (compilation unit)                                 ║
║  ├── Binary crate (has main.rs — produces executable)     ║
║  └── Library crate (has lib.rs — produces library)        ║
║                                                           ║
║  MODULE (code organization within a crate)                ║
║  └── Defined with `mod` keyword                           ║
║                                                           ║
║  ITEM (smallest unit)                                     ║
║  └── fn, struct, enum, trait, const, static, impl, use    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### 2.2 Simple Project Structure

```
my_project/
├── Cargo.toml              # Package manifest
├── Cargo.lock              # Locked dependency versions
├── src/
│   ├── main.rs             # Binary crate root (entry point)
│   └── lib.rs              # Library crate root (optional)
├── tests/
│   └── integration_test.rs # Integration tests
├── benches/
│   └── benchmark.rs        # Benchmarks
├── examples/
│   └── example1.rs         # Example programs
└── target/                 # Build output (gitignored)
    ├── debug/              # Debug builds
    └── release/            # Release builds
```

### 2.3 Complex Project Structure

```
my_project/
├── Cargo.toml
├── src/
│   ├── main.rs              # Entry point
│   ├── lib.rs               # Library root
│   ├── config.rs            # Module file
│   ├── models/              # Module directory
│   │   ├── mod.rs           # Module declaration
│   │   ├── user.rs          # Submodule
│   │   └── product.rs       # Submodule
│   ├── services/
│   │   ├── mod.rs
│   │   ├── auth.rs
│   │   └── database.rs
│   ├── handlers/
│   │   ├── mod.rs
│   │   ├── api.rs
│   │   └── web.rs
│   ├── utils/
│   │   ├── mod.rs
│   │   ├── helpers.rs
│   │   └── validators.rs
│   └── errors.rs
├── tests/
│   ├── api_tests.rs
│   └── db_tests.rs
├── examples/
│   └── basic_usage.rs
├── benches/
│   └── performance.rs
├── migrations/              # DB migrations
├── static/                  # Static files
├── .env                     # Environment variables
├── .gitignore
└── README.md
```

### 2.4 Cargo.toml (Package Manifest)

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"                    # Rust edition (2015, 2018, 2021)
authors = ["Your Name <email@example.com>"]
description = "A description of your project"
license = "MIT"
repository = "https://github.com/user/project"
readme = "README.md"
keywords = ["web", "api", "rust"]
categories = ["web-programming"]

# ── Dependencies (from crates.io) ──
[dependencies]
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tokio = { version = "1", features = ["full"] }
axum = "0.7"
sqlx = { version = "0.7", features = ["runtime-tokio", "postgres"] }
tracing = "0.1"
anyhow = "1.0"
thiserror = "1.0"
chrono = { version = "0.4", features = ["serde"] }
uuid = { version = "1.0", features = ["v4", "serde"] }
reqwest = { version = "0.11", features = ["json"] }
clap = { version = "4", features = ["derive"] }

# Local dependency
my_library = { path = "../my_library" }

# Git dependency
some_crate = { git = "https://github.com/user/repo", branch = "main" }

# ── Dev Dependencies (only for tests/benchmarks) ──
[dev-dependencies]
criterion = "0.5"
mockall = "0.12"
tempfile = "3.0"

# ── Build Dependencies ──
[build-dependencies]
cc = "1.0"                          # For compiling C code

# ── Binary targets ──
[[bin]]
name = "my_app"
path = "src/main.rs"

[[bin]]
name = "my_cli"
path = "src/cli.rs"

# ── Library target ──
[lib]
name = "my_lib"
path = "src/lib.rs"

# ── Features (conditional compilation) ──
[features]
default = ["json"]
json = ["serde_json"]
full = ["json", "database"]
database = ["sqlx"]

# ── Profile settings ──
[profile.dev]
opt-level = 0                       # No optimization (fast compile)
debug = true

[profile.release]
opt-level = 3                       # Maximum optimization
lto = true                          # Link-Time Optimization
strip = true                        # Strip debug symbols
codegen-units = 1                   # Better optimization

# ── Workspace (multi-crate project) ──
[workspace]
members = [
    "crate_a",
    "crate_b",
    "crate_c",
]
```

### 2.5 Module System

```rust
// ═══════════════════════════════════════
// FILE: src/lib.rs (Library root)
// ═══════════════════════════════════════

// Declare modules
pub mod models;          // looks for src/models/mod.rs OR src/models.rs
pub mod services;        // looks for src/services/mod.rs OR src/services.rs
pub mod utils;
mod internal;            // private module (not accessible outside crate)

// Re-export commonly used items
pub use models::user::User;
pub use models::product::Product;
pub use services::auth::authenticate;

// ═══════════════════════════════════════
// FILE: src/models/mod.rs
// ═══════════════════════════════════════

pub mod user;            // looks for src/models/user.rs
pub mod product;         // looks for src/models/product.rs

// ═══════════════════════════════════════
// FILE: src/models/user.rs
// ═══════════════════════════════════════

use serde::{Deserialize, Serialize};
use crate::utils::validators;       // import from another module in same crate

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct User {
    pub id: u64,
    pub username: String,
    pub email: String,
    active: bool,                     // private field
}

impl User {
    pub fn new(id: u64, username: &str, email: &str) -> Result<Self, String> {
        if !validators::is_valid_email(email) {
            return Err(String::from("Invalid email"));
        }
        Ok(User {
            id,
            username: String::from(username),
            email: String::from(email),
            active: true,
        })
    }

    pub fn is_active(&self) -> bool {
        self.active
    }

    pub fn deactivate(&mut self) {
        self.active = false;
    }
}

// ═══════════════════════════════════════
// FILE: src/models/product.rs
// ═══════════════════════════════════════

#[derive(Debug, Clone)]
pub struct Product {
    pub id: u64,
    pub name: String,
    pub price: f64,
}

impl Product {
    pub fn new(id: u64, name: &str, price: f64) -> Self {
        Product {
            id,
            name: String::from(name),
            price,
        }
    }
}

// ═══════════════════════════════════════
// FILE: src/utils/mod.rs
// ═══════════════════════════════════════

pub mod validators;
pub mod helpers;

// ═══════════════════════════════════════
// FILE: src/utils/validators.rs
// ═══════════════════════════════════════

pub fn is_valid_email(email: &str) -> bool {
    email.contains('@') && email.contains('.')
}

pub fn is_valid_username(username: &str) -> bool {
    username.len() >= 3 && username.len() <= 20
}

// ═══════════════════════════════════════
// FILE: src/services/mod.rs
// ═══════════════════════════════════════

pub mod auth;
pub mod database;

// ═══════════════════════════════════════
// FILE: src/services/auth.rs
// ═══════════════════════════════════════

use crate::models::user::User;      // absolute path from crate root
use super::database;                  // relative path (parent module)

pub fn authenticate(username: &str, password: &str) -> Option<User> {
    // Authentication logic
    if password.len() >= 8 {
        Some(User::new(1, username, &format!("{}@example.com", username)).unwrap())
    } else {
        None
    }
}

// ═══════════════════════════════════════
// FILE: src/main.rs (Binary entry point)
// ═══════════════════════════════════════

// Import from our library crate
use my_project::User;
use my_project::Product;
use my_project::authenticate;

// Or use full paths
// use my_project::models::user::User;
// use my_project::services::auth::authenticate;

fn main() {
    let user = User::new(1, "alice", "alice@mail.com").unwrap();
    let product = Product::new(1, "Laptop", 999.99);

    println!("User: {:?}", user);
    println!("Product: {:?}", product);

    if let Some(auth_user) = authenticate("alice", "password123") {
        println!("Authenticated: {:?}", auth_user);
    }
}
```

### Module Path Reference

```
╔═══════════════════════════════════════════════════════════╗
║                   MODULE PATHS                            ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  crate::         → absolute path from crate root          ║
║  self::          → current module                         ║
║  super::         → parent module                          ║
║                                                           ║
║  VISIBILITY:                                              ║
║  (default)       → private (same module only)             ║
║  pub             → public (accessible from outside)       ║
║  pub(crate)      → public within the crate only           ║
║  pub(super)      → public to parent module only           ║
║  pub(in path)    → public to specific module              ║
║                                                           ║
║  USE PATTERNS:                                            ║
║  use std::collections::HashMap;                           ║
║  use std::io::{self, Read, Write};    (multiple items)    ║
║  use std::collections::*;             (glob — avoid)      ║
║  use crate::models::User as UserModel; (rename)           ║
║  pub use crate::models::User;         (re-export)         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### 2.6 Workspace (Multi-Crate Project)

```
my_workspace/
├── Cargo.toml                  # Workspace root
├── crates/
│   ├── core/                   # Shared types/logic
│   │   ├── Cargo.toml
│   │   └── src/lib.rs
│   ├── api/                    # Web API
│   │   ├── Cargo.toml
│   │   └── src/main.rs
│   ├── cli/                    # CLI tool
│   │   ├── Cargo.toml
│   │   └── src/main.rs
│   └── worker/                 # Background worker
│       ├── Cargo.toml
│       └── src/main.rs
└── shared/
    └── utils/
        ├── Cargo.toml
        └── src/lib.rs
```

```toml
# Root Cargo.toml
[workspace]
members = [
    "crates/core",
    "crates/api",
    "crates/cli",
    "crates/worker",
    "shared/utils",
]

# Shared dependencies across workspace
[workspace.dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
```

```toml
# crates/api/Cargo.toml
[package]
name = "api"
version = "0.1.0"
edition = "2021"

[dependencies]
core = { path = "../core" }
utils = { path = "../../shared/utils" }
serde.workspace = true          # use workspace version
tokio.workspace = true
axum = "0.7"
```

---

## PART 3: RUST LIBRARIES (Standard Library & Ecosystem)

### 3.1 Standard Library (std) — Complete Map

```
╔═══════════════════════════════════════════════════════════════╗
║              RUST STANDARD LIBRARY (std)                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  std::                                                        ║
║  │                                                            ║
║  ├── PRIMITIVES (built-in, always available)                  ║
║  │   ├── bool, char, i8-i128, u8-u128, f32, f64              ║
║  │   ├── str, &str, String                                    ║
║  │   ├── array [T; N], slice &[T]                             ║
║  │   ├── tuple (T, U, V)                                      ║
║  │   ├── Option<T>, Result<T,E>                               ║
║  │   └── fn, pointer *const T, *mut T                         ║
║  │                                                            ║
║  ├── COLLECTIONS (std::collections)                           ║
║  │   ├── Vec<T>          Dynamic array                        ║
║  │   ├── VecDeque<T>     Double-ended queue                   ║
║  │   ├── LinkedList<T>   Doubly-linked list                   ║
║  │   ├── HashMap<K,V>    Hash table                           ║
║  │   ├── BTreeMap<K,V>   Sorted map (B-tree)                  ║
║  │   ├── HashSet<T>      Hash set                             ║
║  │   ├── BTreeSet<T>     Sorted set                           ║
║  │   ├── BinaryHeap<T>   Priority queue (max-heap)            ║
║  │   └── String          UTF-8 string                         ║
║  │                                                            ║
║  ├── I/O (std::io)                                            ║
║  │   ├── stdin, stdout, stderr                                ║
║  │   ├── Read, Write, BufRead traits                          ║
║  │   ├── BufReader, BufWriter                                 ║
║  │   ├── Cursor                                               ║
║  │   └── Error, Result                                        ║
║  │                                                            ║
║  ├── FILE SYSTEM (std::fs)                                    ║
║  │   ├── File                                                 ║
║  │   ├── read_to_string, write                                ║
║  │   ├── create_dir, remove_file                              ║
║  │   ├── metadata, permissions                                ║
║  │   ├── copy, rename                                         ║
║  │   └── DirEntry, ReadDir                                    ║
║  │                                                            ║
║  ├── NETWORKING (std::net)                                    ║
║  │   ├── TcpListener, TcpStream                               ║
║  │   ├── UdpSocket                                            ║
║  │   ├── IpAddr, SocketAddr                                   ║
║  │   └── ToSocketAddrs                                        ║
║  │                                                            ║
║  ├── THREADING (std::thread)                                  ║
║  │   ├── spawn, sleep, yield_now                              ║
║  │   ├── JoinHandle                                           ║
║  │   ├── Builder                                              ║
║  │   └── ThreadId                                             ║
║  │                                                            ║
║  ├── SYNC (std::sync)                                         ║
║  │   ├── Arc<T>          Atomic reference counting            ║
║  │   ├── Mutex<T>        Mutual exclusion                     ║
║  │   ├── RwLock<T>       Read-write lock                      ║
║  │   ├── mpsc            Multi-producer single-consumer       ║
║  │   ├── Barrier         Thread synchronization               ║
║  │   ├── Condvar         Condition variable                   ║
║  │   └── Once            One-time initialization              ║
║  │                                                            ║
║  ├── SMART POINTERS                                           ║
║  │   ├── Box<T>          Heap allocation                      ║
║  │   ├── Rc<T>           Reference counting (single-thread)   ║
║  │   ├── Arc<T>          Atomic ref counting (multi-thread)   ║
║  │   ├── Cell<T>         Interior mutability (Copy types)     ║
║  │   ├── RefCell<T>      Interior mutability (any type)       ║
║  │   ├── Cow<T>          Clone on write                       ║
║  │   └── Pin<T>          Pinned memory (for async)            ║
║  │                                                            ║
║  ├── TIME (std::time)                                         ║
║  │   ├── Duration                                             ║
║  │   ├── Instant          Monotonic clock                     ║
║  │   └── SystemTime       Wall clock                          ║
║  │                                                            ║
║  ├── PATH (std::path)                                         ║
║  │   ├── Path             Borrowed path                       ║
║  │   └── PathBuf          Owned path                          ║
║  │                                                            ║
║  ├── ENVIRONMENT (std::env)                                   ║
║  │   ├── args             Command line arguments              ║
║  │   ├── var, set_var     Environment variables               ║
║  │   ├── current_dir      Working directory                   ║
║  │   └── consts           Platform constants                  ║
║  │                                                            ║
║  ├── PROCESS (std::process)                                   ║
║  │   ├── Command          Spawn external processes            ║
║  │   ├── exit             Exit program                        ║
║  │   ├── Stdio            Stdin/out/err config                ║
║  │   └── Child            Child process handle                ║
║  │                                                            ║
║  ├── CONVERSION TRAITS                                        ║
║  │   ├── From / Into                                          ║
║  │   ├── TryFrom / TryInto                                    ║
║  │   ├── AsRef / AsMut                                        ║
║  │   └── ToString / FromStr                                   ║
║  │                                                            ║
║  ├── OPERATOR TRAITS (std::ops)                               ║
║  │   ├── Add, Sub, Mul, Div, Rem                              ║
║  │   ├── Neg, Not                                             ║
║  │   ├── Index, IndexMut                                      ║
║  │   ├── Deref, DerefMut                                      ║
║  │   └── Drop                                                 ║
║  │                                                            ║
║  ├── FORMATTING (std::fmt)                                    ║
║  │   ├── Display          {} formatting                       ║
║  │   ├── Debug            {:?} formatting                     ║
║  │   └── Write            write! target                       ║
║  │                                                            ║
║  ├── ITERATORS (std::iter)                                    ║
║  │   ├── Iterator trait                                       ║
║  │   ├── IntoIterator                                         ║
║  │   ├── FromIterator                                         ║
║  │   └── Adapters: map, filter, fold, zip, chain, etc.        ║
║  │                                                            ║
║  ├── MARKER TRAITS (std::marker)                              ║
║  │   ├── Send             Safe to send between threads        ║
║  │   ├── Sync             Safe to share between threads       ║
║  │   ├── Copy             Implicit copy (stack types)         ║
║  │   ├── Sized            Known size at compile time          ║
║  │   └── Unpin            Can be moved in memory              ║
║  │                                                            ║
║  └── ERROR (std::error)                                       ║
║      └── Error trait      Standard error interface             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### 3.2 Standard Library Usage Examples

```rust
// ═══════════════════════════════════════
// FILE I/O
// ═══════════════════════════════════════
use std::fs;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Write, BufWriter, Read};
use std::path::Path;

fn file_operations() -> io::Result<()> {
    // Write to file
    fs::write("output.txt", "Hello, World!")?;

    // Read entire file
    let content = fs::read_to_string("output.txt")?;
    println!("{}", content);

    // Read file line by line
    let file = File::open("output.txt")?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        println!("Line: {}", line?);
    }

    // Write with buffering
    let file = File::create("buffered.txt")?;
    let mut writer = BufWriter::new(file);
    writeln!(writer, "Line 1")?;
    writeln!(writer, "Line 2")?;
    writer.flush()?;

    // Append to file
    let mut file = fs::OpenOptions::new()
        .append(true)
        .open("output.txt")?;
    writeln!(file, "\nAppended line")?;

    // File metadata
    let metadata = fs::metadata("output.txt")?;
    println!("Size: {} bytes", metadata.len());
    println!("Is file: {}", metadata.is_file());
    println!("Modified: {:?}", metadata.modified()?);

    // Directory operations
    fs::create_dir_all("data/subdir")?;

    // List directory
    for entry in fs::read_dir(".")? {
        let entry = entry?;
        println!("{:?} - {:?}", entry.file_name(), entry.file_type()?);
    }

    // Copy and rename
    fs::copy("output.txt", "backup.txt")?;
    fs::rename("backup.txt", "archive.txt")?;

    // Remove
    fs::remove_file("archive.txt")?;
    // fs::remove_dir_all("data")?;

    Ok(())
}

// ═══════════════════════════════════════
// NETWORKING
// ═══════════════════════════════════════
use std::net::{TcpListener, TcpStream, UdpSocket};

fn tcp_server() -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8080")?;
    println!("Server listening on port 8080");

    for stream in listener.incoming() {
        let mut stream = stream?;
        let mut buffer = [0; 1024];
        let bytes_read = stream.read(&mut buffer)?;
        let request = String::from_utf8_lossy(&buffer[..bytes_read]);
        println!("Received: {}", request);

        let response = "HTTP/1.1 200 OK\r\n\r\nHello from Rust!";
        stream.write_all(response.as_bytes())?;
    }
    Ok(())
}

fn tcp_client() -> io::Result<()> {
    let mut stream = TcpStream::connect("127.0.0.1:8080")?;
    stream.write_all(b"Hello, Server!")?;

    let mut response = String::new();
    stream.read_to_string(&mut response)?;
    println!("Response: {}", response);
    Ok(())
}

// ═══════════════════════════════════════
// THREADING
// ═══════════════════════════════════════
use std::thread;
use std::sync::{Arc, Mutex, mpsc};
use std::time::Duration;

fn threading_examples() {
    // Basic thread
    let handle = thread::spawn(|| {
        for i in 1..5 {
            println!("Thread: {}", i);
            thread::sleep(Duration::from_millis(100));
        }
        42  // return value
    });

    let result = handle.join().unwrap();
    println!("Thread returned: {}", result);

    // Thread with data (move)
    let data = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        println!("Data from thread: {:?}", data);
    });
    handle.join().unwrap();

    // Shared state with Arc<Mutex<T>>
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("Counter: {}", *counter.lock().unwrap());

    // Channels (message passing)
    let (tx, rx) = mpsc::channel();

    // Multiple producers
    for i in 0..5 {
        let tx = tx.clone();
        thread::spawn(move || {
            tx.send(format!("Message {}", i)).unwrap();
        });
    }
    drop(tx);  // drop original sender

    for received in rx {
        println!("Got: {}", received);
    }
}

// ═══════════════════════════════════════
// PROCESS (External Commands)
// ═══════════════════════════════════════
use std::process::Command;

fn process_examples() -> io::Result<()> {
    // Run a command
    let output = Command::new("echo")
        .arg("Hello from Rust!")
        .output()?;

    println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
    println!("status: {}", output.status);

    // Run with piped I/O
    let output = Command::new("ls")
        .arg("-la")
        .output()?;

    if output.status.success() {
        println!("{}", String::from_utf8_lossy(&output.stdout));
    } else {
        eprintln!("{}", String::from_utf8_lossy(&output.stderr));
    }

    // Check if command exists
    let status = Command::new("rustc")
        .arg("--version")
        .status()?;
    println!("rustc available: {}", status.success());

    Ok(())
}

// ═══════════════════════════════════════
// ENVIRONMENT
// ═══════════════════════════════════════
use std::env;

fn env_examples() {
    // Command line arguments
    let args: Vec<String> = env::args().collect();
    println!("Program: {}", args[0]);
    for (i, arg) in args.iter().enumerate().skip(1) {
        println!("Arg {}: {}", i, arg);
    }

    // Environment variables
    match env::var("HOME") {
        Ok(val) => println!("HOME: {}", val),
        Err(_) => println!("HOME not set"),
    }

    // Current directory
    let cwd = env::current_dir().unwrap();
    println!("Current dir: {:?}", cwd);

    // Platform info
    println!("OS: {}", env::consts::OS);           // linux, macos, windows
    println!("Arch: {}", env::consts::ARCH);       // x86_64, aarch64
    println!("Family: {}", env::consts::FAMILY);   // unix, windows
}

// ═══════════════════════════════════════
// TIME
// ═══════════════════════════════════════
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

fn time_examples() {
    // Measure elapsed time
    let start = Instant::now();
    // ... do work ...
    thread::sleep(Duration::from_millis(100));
    let elapsed = start.elapsed();
    println!("Elapsed: {:?}", elapsed);
    println!("Elapsed ms: {}", elapsed.as_millis());

    // System time (wall clock)
    let now = SystemTime::now();
    let since_epoch = now.duration_since(UNIX_EPOCH).unwrap();
    println!("Unix timestamp: {}", since_epoch.as_secs());

    // Duration
    let five_secs = Duration::from_secs(5);
    let half_sec = Duration::from_millis(500);
    let total = five_secs + half_sec;
    println!("Total: {:?}", total);
}

// ═══════════════════════════════════════
// PATH
// ═══════════════════════════════════════
use std::path::{Path, PathBuf};

fn path_examples() {
    // Create paths
    let path = Path::new("/home/user/documents/file.txt");

    println!("File name: {:?}", path.file_name());        // Some("file.txt")
    println!("Extension: {:?}", path.extension());          // Some("txt")
    println!("Stem: {:?}", path.file_stem());              // Some("file")
    println!("Parent: {:?}", path.parent());               // Some("/home/user/documents")
    println!("Is absolute: {}", path.is_absolute());       // true
    println!("Exists: {}", path.exists());

    // Build paths
    let mut path = PathBuf::from("/home/user");
    path.push("documents");
    path.push("file.txt");
    println!("Built: {:?}", path);

    // Join
    let base = Path::new("/home/user");
    let full = base.join("documents").join("file.txt");
    println!("Joined: {:?}", full);

    // Components
    for component in Path::new("/home/user/file.txt").components() {
        println!("Component: {:?}", component);
    }
}

fn main() {
    env_examples();
    time_examples();
    path_examples();
    // file_operations().unwrap();
    // threading_examples();
}
```

### 3.3 Popular Ecosystem Crates (External Libraries)

```
╔═══════════════════════════════════════════════════════════════════╗
║                RUST ECOSYSTEM — TOP CRATES                       ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ── SERIALIZATION ──                                              ║
║  serde           Framework for serialize/deserialize              ║
║  serde_json      JSON support                                     ║
║  serde_yaml      YAML support                                     ║
║  toml            TOML support                                     ║
║  csv             CSV support                                      ║
║  bincode         Binary serialization                             ║
║                                                                   ║
║  ── WEB FRAMEWORKS ──                                             ║
║  axum            Modern web framework (by Tokio team)             ║
║  actix-web       High-performance web framework                   ║
║  rocket          Easy-to-use web framework                        ║
║  warp            Composable web framework                         ║
║  poem            Another modern web framework                     ║
║                                                                   ║
║  ── HTTP CLIENT ──                                                ║
║  reqwest         High-level HTTP client                           ║
║  hyper           Low-level HTTP library                           ║
║  ureq            Simple blocking HTTP client                      ║
║                                                                   ║
║  ── ASYNC RUNTIME ──                                              ║
║  tokio           Most popular async runtime                       ║
║  async-std       Alternative async runtime                        ║
║  smol            Small async runtime                              ║
║                                                                   ║
║  ── DATABASE ──                                                   ║
║  sqlx            Async SQL (compile-time checked queries!)        ║
║  diesel          ORM and query builder                            ║
║  sea-orm         Async ORM                                        ║
║  rusqlite        SQLite bindings                                  ║
║  redis           Redis client                                     ║
║  mongodb         MongoDB driver                                   ║
║                                                                   ║
║  ── CLI ──                                                        ║
║  clap            Command line argument parser                     ║
║  dialoguer       Interactive CLI prompts                          ║
║  indicatif       Progress bars                                    ║
║  colored         Terminal colors                                  ║
║  tui / ratatui   Terminal UI framework                            ║
║                                                                   ║
║  ── ERROR HANDLING ──                                             ║
║  anyhow          Easy error handling (applications)               ║
║  thiserror       Derive custom error types (libraries)            ║
║  eyre            Alternative to anyhow                            ║
║                                                                   ║
║  ── LOGGING & TRACING ──                                          ║
║  tracing         Structured logging & diagnostics                 ║
║  log             Logging facade                                   ║
║  env_logger      Simple logger                                    ║
║  tracing-subscriber  Tracing output                               ║
║                                                                   ║
║  ── TESTING ──                                                    ║
║  mockall         Mocking framework                                ║
║  proptest        Property-based testing                           ║
║  criterion       Benchmarking                                     ║
║  fake            Generate fake data                               ║
║  wiremock        HTTP mocking                                     ║
║                                                                   ║
║  ── CRYPTOGRAPHY ──                                               ║
║  ring            Crypto primitives                                ║
║  rustls          TLS library (pure Rust)                          ║
║  argon2          Password hashing                                 ║
║  jsonwebtoken    JWT tokens                                       ║
║  bcrypt          Password hashing                                 ║
║                                                                   ║
║  ── DATA & MATH ──                                                ║
║  regex           Regular expressions                              ║
║  chrono          Date and time                                    ║
║  uuid            UUID generation                                  ║
║  rand            Random number generation                         ║
║  num             Numeric types and traits                         ║
║  ndarray         N-dimensional arrays (like NumPy)                ║
║  polars          DataFrame library (like Pandas)                  ║
║                                                                   ║
║  ── CONCURRENCY ──                                                ║
║  rayon           Data parallelism (parallel iterators)            ║
║  crossbeam       Advanced concurrency primitives                  ║
║  parking_lot     Faster Mutex/RwLock                              ║
║  dashmap         Concurrent HashMap                               ║
║                                                                   ║
║  ── SYSTEMS ──                                                    ║
║  libc            C standard library bindings                      ║
║  nix             Unix API bindings                                ║
║  winapi          Windows API bindings                             ║
║  bytes           Efficient byte buffer                            ║
║  memmap2         Memory-mapped files                              ║
║                                                                   ║
║  ── WASM ──                                                       ║
║  wasm-bindgen    Rust ↔ JavaScript interop                       ║
║  web-sys         Web API bindings                                 ║
║  yew             Frontend framework (like React)                  ║
║  leptos          Full-stack web framework                         ║
║  trunk           WASM build tool                                  ║
║                                                                   ║
║  ── GAME DEV ──                                                   ║
║  bevy            Game engine                                      ║
║  macroquad       Simple game library                              ║
║  ggez            2D game framework                                ║
║  wgpu            GPU graphics API                                 ║
║                                                                   ║
║  ── EMBEDDED ──                                                   ║
║  embedded-hal    Hardware abstraction layer                       ║
║  cortex-m        ARM Cortex-M support                             ║
║  esp-hal         ESP32 support                                    ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 3.4 Crate Usage Examples

```rust
// ═══════════════════════════════════════
// Cargo.toml dependencies
// ═══════════════════════════════════════
// [dependencies]
// serde = { version = "1.0", features = ["derive"] }
// serde_json = "1.0"
// reqwest = { version = "0.11", features = ["json"] }
// tokio = { version = "1", features = ["full"] }
// chrono = { version = "0.4", features = ["serde"] }
// uuid = { version = "1", features = ["v4"] }
// rand = "0.8"
// regex = "1"
// clap = { version = "4", features = ["derive"] }
// anyhow = "1.0"
// tracing = "0.1"

// ═══════════════════════════════════════
// SERDE — Serialization/Deserialization
// ═══════════════════════════════════════
use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize)]
struct User {
    name: String,
    age: u32,
    email: String,
    #[serde(default)]
    active: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    nickname: Option<String>,
}

fn serde_example() {
    let user = User {
        name: "Alice".to_string(),
        age: 30,
        email: "alice@mail.com".to_string(),
        active: true,
        nickname: Some("Ali".to_string()),
    };

    // Struct → JSON string
    let json = serde_json::to_string_pretty(&user).unwrap();
    println!("JSON:\n{}", json);

    // JSON string → Struct
    let json_str = r#"{"name":"Bob","age":25,"email":"bob@mail.com"}"#;
    let user: User = serde_json::from_str(json_str).unwrap();
    println!("Parsed: {:?}", user);

    // Struct → JSON Value (dynamic)
    let value: serde_json::Value = serde_json::json!({
        "name": "Charlie",
        "scores": [90, 85, 92],
        "metadata": {
            "source": "api"
        }
    });
    println!("Name: {}", value["name"]);
    println!("First score: {}", value["scores"][0]);

    // File I/O with serde
    let user = User {
        name: "Dave".to_string(),
        age: 35,
        email: "dave@mail.com".to_string(),
        active: true,
        nickname: None,
    };
    // Write to file
    let file = std::fs::File::create("user.json").unwrap();
    serde_json::to_writer_pretty(file, &user).unwrap();

    // Read from file
    let file = std::fs::File::open("user.json").unwrap();
    let loaded: User = serde_json::from_reader(file).unwrap();
    println!("Loaded: {:?}", loaded);
}

// ═══════════════════════════════════════
// REGEX — Regular Expressions
// ═══════════════════════════════════════
use regex::Regex;

fn regex_example() {
    let re = Regex::new(r"\b\w{4}\b").unwrap();   // 4-letter words

    let text = "The quick brown fox jumps over the lazy dog";

    // Find all matches
    for mat in re.find_iter(text) {
        println!("Found: '{}' at {}-{}", mat.as_str(), mat.start(), mat.end());
    }

    // Capture groups
    let re = Regex::new(r"(\w+)@(\w+)\.(\w+)").unwrap();
    let email = "user@example.com";

    if let Some(caps) = re.captures(email) {
        println!("User: {}", &caps[1]);
        println!("Domain: {}", &caps[2]);
        println!("TLD: {}", &caps[3]);
    }

    // Replace
    let re = Regex::new(r"\d+").unwrap();
    let result = re.replace_all("call 123-456-7890", "[REDACTED]");
    println!("{}", result);

    // Check if matches
    let re = Regex::new(r"^\d{3}-\d{3}-\d{4}$").unwrap();
    println!("Valid phone: {}", re.is_match("123-456-7890"));
}

// ═══════════════════════════════════════
// RAND — Random Numbers
// ═══════════════════════════════════════
use rand::Rng;
use rand::seq::SliceRandom;

fn rand_example() {
    let mut rng = rand::thread_rng();

    // Random numbers
    let n: i32 = rng.gen_range(1..=100);
    let f: f64 = rng.gen();                    // 0.0 to 1.0
    let b: bool = rng.gen();

    println!("Random int: {}", n);
    println!("Random float: {:.4}", f);
    println!("Random bool: {}", b);

    // Shuffle
    let mut cards = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    cards.shuffle(&mut rng);
    println!("Shuffled: {:?}", cards);

    // Random choice
    let fruits = ["apple", "banana", "cherry", "date"];
    let choice = fruits.choose(&mut rng).unwrap();
    println!("Random fruit: {}", choice);
}

// ═══════════════════════════════════════
// CHRONO — Date & Time
// ═══════════════════════════════════════
use chrono::{Utc, Local, NaiveDate, Duration as ChronoDuration, Datelike, Timelike};

fn chrono_example() {
    // Current time
    let utc_now = Utc::now();
    let local_now = Local::now();
    println!("UTC: {}", utc_now);
    println!("Local: {}", local_now);

    // Formatting
    println!("Formatted: {}", local_now.format("%Y-%m-%d %H:%M:%S"));
    println!("Date only: {}", local_now.format("%B %d, %Y"));

    // Components
    println!("Year: {}", local_now.year());
    println!("Month: {}", local_now.month());
    println!("Day: {}", local_now.day());
    println!("Hour: {}", local_now.hour());

    // Create specific date
    let date = NaiveDate::from_ymd_opt(2024, 12, 25).unwrap();
    println!("Christmas: {}", date);

    // Duration
    let tomorrow = local_now + ChronoDuration::days(1);
    let last_week = local_now - ChronoDuration::weeks(1);
    println!("Tomorrow: {}", tomorrow.format("%Y-%m-%d"));
    println!("Last week: {}", last_week.format("%Y-%m-%d"));

    // Parse from string
    let parsed = NaiveDate::parse_from_str("2024-06-15", "%Y-%m-%d").unwrap();
    println!("Parsed: {}", parsed);
}

// ═══════════════════════════════════════
// CLAP — CLI Argument Parser
// ═══════════════════════════════════════
use clap::Parser;

#[derive(Parser, Debug)]
#[command(name = "myapp", about = "A sample CLI app")]
struct Args {
    /// Name of the user
    #[arg(short, long)]
    name: String,

    /// Age of the user
    #[arg(short, long, default_value_t = 0)]
    age: u32,

    /// Enable verbose output
    #[arg(short, long)]
    verbose: bool,

    /// Files to process
    #[arg(required = true)]
    files: Vec<String>,
}

fn clap_example() {
    let args = Args::parse();
    println!("Name: {}", args.name);
    println!("Age: {}", args.age);
    println!("Verbose: {}", args.verbose);
    println!("Files: {:?}", args.files);
}

// Usage: myapp --name Alice --age 30 --verbose file1.txt file2.txt

// ═══════════════════════════════════════
// ANYHOW — Error Handling (for applications)
// ═══════════════════════════════════════
use anyhow::{Context, Result, bail, ensure};

fn anyhow_example() -> Result<()> {
    // Automatically converts any error type
    let content = std::fs::read_to_string("config.toml")
        .context


╔═══════════════════════════════════════════════════════════════════╗
║              REAL-WORLD RUST


# 🦀 Rust Hardware Guide (Continued)

---

## PART 6: REAL-WORLD HARDWARE DEPLOYMENTS (Continued)

### 6.1 Companies Using Rust on Various Hardware

```
╔═══════════════════════════════════════════════════════════════════╗
║              REAL-WORLD RUST DEPLOYMENTS                          ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ── CLOUD / SERVERS ──                                            ║
║  │                                                                ║
║  ├── Amazon (AWS)                                                 ║
║  │   ├── Firecracker — microVM (powers Lambda & Fargate)          ║
║  │   ├── Bottlerocket — container-focused Linux OS                ║
║  │   ├── S3 — object storage components                           ║
║  │   ├── CloudFront — CDN                                         ║
║  │   └── Hardware: x86_64, ARM64 (Graviton)                      ║
║  │                                                                ║
║  ├── Microsoft                                                    ║
║  │   ├── Azure IoT Edge                                           ║
║  │   ├── Windows kernel components                                ║
║  │   ├── VS Code search (ripgrep)                                 ║
║  │   └── Hardware: x86_64, ARM64                                  ║
║  │                                                                ║
║  ├── Google                                                       ║
║  │   ├── Android OS (Rust in kernel & userspace)                  ║
║  │   ├── Chrome OS                                                ║
║  │   ├── Fuchsia OS                                               ║
║  │   ├── gVisor (container sandbox)                               ║
║  │   └── Hardware: x86_64, ARM64, ARM (mobile)                   ║
║  │                                                                ║
║  ├── Cloudflare                                                   ║
║  │   ├── Pingora — HTTP proxy (replaced nginx)                    ║
║  │   ├── Workers runtime                                          ║
║  │   ├── DNS resolver                                             ║
║  │   ├── Firewall rules engine                                    ║
║  │   └── Hardware: x86_64 servers, edge network worldwide         ║
║  │                                                                ║
║  ├── Meta (Facebook)                                              ║
║  │   ├── Source control (Mononoke — Mercurial server)             ║
║  │   ├── Buck2 — build system                                     ║
║  │   └── Hardware: x86_64 data center servers                     ║
║  │                                                                ║
║  ├── Discord                                                      ║
║  │   ├── Read States service (moved from Go to Rust)              ║
║  │   ├── Various backend services                                 ║
║  │   └── Hardware: x86_64 servers                                 ║
║  │                                                                ║
║  ├── Dropbox                                                      ║
║  │   ├── File sync engine                                         ║
║  │   ├── Storage compression                                     ║
║  │   └── Hardware: x86_64 servers, desktop (Win/Mac/Linux)       ║
║  │                                                                ║
║  └── Netflix, Figma, Shopify, Vercel, 1Password...               ║
║                                                                   ║
║  ── OPERATING SYSTEMS ──                                          ║
║  │                                                                ║
║  ├── Linux Kernel (Rust merged since 6.1)                         ║
║  │   └── Hardware: ALL Linux-supported architectures              ║
║  ├── Android (Rust in AOSP since Android 12)                      ║
║  │   └── Hardware: ARM64, ARM32 phones & tablets                  ║
║  ├── Windows (Rust in kernel since 2023)                          ║
║  │   └── Hardware: x86_64, ARM64                                  ║
║  ├── Redox OS (entire OS written in Rust)                         ║
║  │   └── Hardware: x86_64, i686                                   ║
║  ├── Theseus OS (research OS in Rust)                             ║
║  │   └── Hardware: x86_64                                         ║
║  ├── Tock OS (embedded OS in Rust)                                ║
║  │   └── Hardware: ARM Cortex-M, RISC-V                          ║
║  └── Hubris (Oxide Computer — embedded OS)                        ║
║      └── Hardware: ARM Cortex-M                                   ║
║                                                                   ║
║  ── EMBEDDED / IoT ──                                             ║
║  │                                                                ║
║  ├── Oxide Computer Company                                       ║
║  │   ├── Custom server hardware + Rust firmware                   ║
║  │   ├── Hubris RTOS (Rust-based)                                 ║
║  │   └── Hardware: ARM Cortex-M, AMD EPYC                        ║
║  │                                                                ║
║  ├── Espressif (ESP32 manufacturer)                               ║
║  │   ├── Official Rust support for ESP32 family                   ║
║  │   └── Hardware: ESP32, ESP32-S2/S3, ESP32-C3/C6               ║
║  │                                                                ║
║  ├── Nordic Semiconductor                                         ║
║  │   ├── Embassy framework for nRF chips                          ║
║  │   └── Hardware: nRF52, nRF53, nRF91 series                    ║
║  │                                                                ║
║  ├── Ferrous Systems (Embedded Rust consultancy)                  ║
║  │   ├── Training & tooling for embedded Rust                     ║
║  │   ├── probe-rs debugging toolkit                               ║
║  │   └── Hardware: Various ARM, RISC-V                            ║
║  │                                                                ║
║  └── Various startups using Rust for IoT devices                  ║
║                                                                   ║
║  ── AUTOMOTIVE ──                                                 ║
║  │                                                                ║
║  ├── Volvo                                                        ║
║  │   ├── Low-energy vehicle software                              ║
║  │   └── Hardware: ARM-based ECUs                                 ║
║  ├── Toyota (connected services)                                  ║
║  ├── Volkswagen Group (exploring)                                 ║
║  ├── Woven by Toyota (Arene platform)                             ║
║  └── Various autonomous driving companies                         ║
║                                                                   ║
║  ── AEROSPACE & DEFENSE ──                                        ║
║  │                                                                ║
║  ├── Aerorust community (aerospace in Rust)                       ║
║  ├── NASA JPL (exploring Rust for flight software)                ║
║  └── Various defense contractors                                  ║
║                                                                   ║
║  ── BLOCKCHAIN ──                                                 ║
║  │                                                                ║
║  ├── Solana (blockchain runtime)                                  ║
║  ├── Polkadot / Substrate (blockchain framework)                  ║
║  ├── NEAR Protocol                                                ║
║  ├── Diem/Libra (Facebook's blockchain, now Aptos)                ║
║  └── Hardware: x86_64, ARM64 validators                           ║
║                                                                   ║
║  ── NETWORKING / CDN ──                                           ║
║  │                                                                ║
║  ├── Cloudflare (see above)                                       ║
║  ├── Fastly (Compute@Edge — WASM)                                 ║
║  ├── Fly.io (edge computing)                                      ║
║  └── Linkerd (service mesh — CNCF project)                        ║
║                                                                   ║
║  ── DATABASES ──                                                  ║
║  │                                                                ║
║  ├── TiKV (distributed key-value, used by TiDB)                   ║
║  ├── SurrealDB (multi-model database)                              ║
║  ├── Qdrant (vector database)                                     ║
║  ├── Meilisearch (search engine)                                  ║
║  ├── Neon (serverless Postgres)                                   ║
║  └── Hardware: x86_64, ARM64 servers                              ║
║                                                                   ║
║  ── DEVELOPER TOOLS ──                                            ║
║  │                                                                ║
║  ├── ripgrep (faster grep — used in VS Code)                      ║
║  ├── fd (faster find)                                             ║
║  ├── bat (better cat)                                             ║
║  ├── exa/eza (better ls)                                          ║
║  ├── delta (better diff)                                          ║
║  ├── starship (shell prompt)                                      ║
║  ├── zoxide (smarter cd)                                          ║
║  ├── Alacritty (GPU terminal)                                     ║
║  ├── Wezterm (terminal emulator)                                  ║
║  ├── Helix (text editor)                                          ║
║  ├── Zed (code editor)                                            ║
║  ├── SWC (JS/TS compiler — used by Next.js)                      ║
║  ├── Turbopack (JS bundler by Vercel)                             ║
║  ├── Deno (JS/TS runtime)                                        ║
║  └── Hardware: x86_64, ARM64 (all desktop platforms)              ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## PART 7: EXTERNAL TOOL COMMUNICATION (FFI & Interop)

### 7.1 How Rust Communicates with External Systems

```
╔═══════════════════════════════════════════════════════════════════╗
║          RUST EXTERNAL COMMUNICATION METHODS                      ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ┌─────────┐     FFI (C ABI)      ┌──────────┐                   ║
║  │  Rust   │◄──────────────────────►│   C/C++  │                  ║
║  └─────────┘                       └──────────┘                   ║
║       │                                                           ║
║       │         wasm-bindgen       ┌──────────┐                   ║
║       ├────────────────────────────►│JavaScript│                  ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │         PyO3 / maturin     ┌──────────┐                   ║
║       ├────────────────────────────►│  Python  │                  ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │         JNI / jni crate    ┌──────────┐                   ║
║       ├────────────────────────────►│   Java   │                  ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │         neon               ┌──────────┐                   ║
║       ├────────────────────────────►│  Node.js │                  ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │         UniFFI             ┌──────────┐                   ║
║       ├────────────────────────────►│Swift/    │                  ║
║       │                            │Kotlin/   │                   ║
║       │                            │Python    │                   ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │     HTTP/gRPC/WebSocket    ┌──────────┐                   ║
║       ├────────────────────────────►│ Any Lang │                  ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │     stdin/stdout/pipe      ┌──────────┐                   ║
║       ├────────────────────────────►│ Any Tool │                  ║
║       │                            └──────────┘                   ║
║       │                                                           ║
║       │     Shared Memory/IPC      ┌──────────┐                   ║
║       └────────────────────────────►│ Any Proc │                  ║
║                                    └──────────┘                   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 7.2 FFI — C Interoperability (Most Important)

```rust
// ═══════════════════════════════════════
// CALLING C FROM RUST
// ═══════════════════════════════════════

// Method 1: Declare external C functions manually
extern "C" {
    fn abs(input: i32) -> i32;
    fn sqrt(input: f64) -> f64;
    fn strlen(s: *const std::os::raw::c_char) -> usize;
    fn printf(format: *const std::os::raw::c_char, ...) -> i32;
}

fn call_c_functions() {
    unsafe {
        println!("abs(-42) = {}", abs(-42));
        println!("sqrt(144) = {}", sqrt(144.0));

        let c_string = std::ffi::CString::new("Hello from C!").unwrap();
        println!("strlen = {}", strlen(c_string.as_ptr()));
    }
}

// Method 2: Using libc crate (comprehensive C bindings)
// Cargo.toml: libc = "0.2"
use libc;

fn using_libc() {
    unsafe {
        // Get process ID
        let pid = libc::getpid();
        println!("PID: {}", pid);

        // Memory allocation (normally don't do this in Rust!)
        let ptr = libc::malloc(100) as *mut u8;
        if !ptr.is_null() {
            *ptr = 42;
            println!("Value: {}", *ptr);
            libc::free(ptr as *mut libc::c_void);
        }

        // Get environment variable
        let key = std::ffi::CString::new("HOME").unwrap();
        let val = libc::getenv(key.as_ptr());
        if !val.is_null() {
            let home = std::ffi::CStr::from_ptr(val);
            println!("HOME: {:?}", home);
        }
    }
}

// Method 3: Binding a C library using bindgen
// build.rs (build script)
// fn main() {
//     println!("cargo:rustc-link-lib=mylib");
//     println!("cargo:rerun-if-changed=wrapper.h");
//     
//     let bindings = bindgen::Builder::default()
//         .header("wrapper.h")
//         .generate()
//         .expect("Unable to generate bindings");
//     
//     let out_path = std::path::PathBuf::from(std::env::var("OUT_DIR").unwrap());
//     bindings.write_to_file(out_path.join("bindings.rs")).unwrap();
// }

// Method 4: Linking a C library manually
// Cargo.toml:
// [build-dependencies]
// cc = "1.0"

// build.rs:
// fn main() {
//     cc::Build::new()
//         .file("src/helper.c")
//         .compile("helper");
// }
```

```c
// src/helper.c — C code compiled alongside Rust
#include <stdio.h>
#include <math.h>

int fast_multiply(int a, int b) {
    return a * b;
}

double compute_distance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx*dx + dy*dy);
}

void print_from_c(const char* message) {
    printf("C says: %s\n", message);
}
```

```rust
// Declare the C functions in Rust
extern "C" {
    fn fast_multiply(a: i32, b: i32) -> i32;
    fn compute_distance(x1: f64, y1: f64, x2: f64, y2: f64) -> f64;
    fn print_from_c(message: *const std::os::raw::c_char);
}

fn main() {
    unsafe {
        let result = fast_multiply(6, 7);
        println!("6 * 7 = {}", result);

        let dist = compute_distance(0.0, 0.0, 3.0, 4.0);
        println!("Distance: {}", dist);

        let msg = std::ffi::CString::new("Hello from Rust!").unwrap();
        print_from_c(msg.as_ptr());
    }
}
```

```rust
// ═══════════════════════════════════════
// EXPOSING RUST TO C (Making Rust callable from C)
// ═══════════════════════════════════════

// Cargo.toml:
// [lib]
// crate-type = ["cdylib", "staticlib"]

use std::ffi::{CStr, CString};
use std::os::raw::{c_char, c_int, c_double};

/// Add two integers — callable from C
#[no_mangle]
pub extern "C" fn rust_add(a: c_int, b: c_int) -> c_int {
    a + b
}

/// Process a string — callable from C
#[no_mangle]
pub extern "C" fn rust_to_uppercase(input: *const c_char) -> *mut c_char {
    if input.is_null() {
        return std::ptr::null_mut();
    }

    let c_str = unsafe { CStr::from_ptr(input) };
    let rust_str = c_str.to_str().unwrap_or("");
    let upper = rust_str.to_uppercase();

    CString::new(upper).unwrap().into_raw()
}

/// Free a string allocated by Rust — must be called from C
#[no_mangle]
pub extern "C" fn rust_free_string(ptr: *mut c_char) {
    if !ptr.is_null() {
        unsafe {
            let _ = CString::from_raw(ptr);
        }
    }
}

/// Compute fibonacci — callable from C
#[no_mangle]
pub extern "C" fn rust_fibonacci(n: c_int) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a: u64 = 0;
            let mut b: u64 = 1;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

// Generated C header (my_rust_lib.h):
// int32_t rust_add(int32_t a, int32_t b);
// char* rust_to_uppercase(const char* input);
// void rust_free_string(char* ptr);
// uint64_t rust_fibonacci(int32_t n);
```

```c
// Using Rust library from C
// main.c
#include <stdio.h>
#include <stdint.h>

// Declare Rust functions
extern int32_t rust_add(int32_t a, int32_t b);
extern char* rust_to_uppercase(const char* input);
extern void rust_free_string(char* ptr);
extern uint64_t rust_fibonacci(int32_t n);

int main() {
    // Call Rust functions from C
    printf("rust_add(3, 4) = %d\n", rust_add(3, 4));

    char* upper = rust_to_uppercase("hello from c");
    printf("Uppercase: %s\n", upper);
    rust_free_string(upper);  // Free Rust-allocated memory

    printf("fib(50) = %lu\n", rust_fibonacci(50));

    return 0;
}

// Compile:
// cargo build --release
// gcc main.c -L target/release -lmy_rust_lib -o myapp
// ./myapp
```

### 7.3 Python Interop (PyO3)

```rust
// ═══════════════════════════════════════
// Cargo.toml
// [package]
// name = "my_python_module"
// version = "0.1.0"
// edition = "2021"
//
// [lib]
// name = "my_python_module"
// crate-type = ["cdylib"]
//
// [dependencies]
// pyo3 = { version = "0.20", features = ["extension-module"] }
// ═══════════════════════════════════════

use pyo3::prelude::*;
use pyo3::types::PyList;

/// A fast Fibonacci function written in Rust
#[pyfunction]
fn fibonacci(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a: u64 = 0;
            let mut b: u64 = 1;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

/// Sum a list of numbers (10-100x faster than Python)
#[pyfunction]
fn fast_sum(numbers: Vec<f64>) -> f64 {
    numbers.iter().sum()
}

/// Count words in text
#[pyfunction]
fn word_count(text: &str) -> std::collections::HashMap<String, usize> {
    let mut counts = std::collections::HashMap::new();
    for word in text.split_whitespace() {
        *counts.entry(word.to_lowercase()).or_insert(0) += 1;
    }
    counts
}

/// A Rust class exposed to Python
#[pyclass]
struct RustCalculator {
    history: Vec<f64>,
}

#[pymethods]
impl RustCalculator {
    #[new]
    fn new() -> Self {
        RustCalculator { history: Vec::new() }
    }

    fn add(&mut self, a: f64, b: f64) -> f64 {
        let result = a + b;
        self.history.push(result);
        result
    }

    fn multiply(&mut self, a: f64, b: f64) -> f64 {
        let result = a * b;
        self.history.push(result);
        result
    }

    fn get_history(&self) -> Vec<f64> {
        self.history.clone()
    }

    fn clear_history(&mut self) {
        self.history.clear();
    }
}

/// Python module definition
#[pymodule]
fn my_python_module(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(fast_sum, m)?)?;
    m.add_function(wrap_pyfunction!(word_count, m)?)?;
    m.add_class::<RustCalculator>()?;
    Ok(())
}
```

```python
# Using the Rust module in Python
# Build with: maturin develop (or maturin build)
# pip install maturin

import my_python_module

# Call Rust functions
print(my_python_module.fibonacci(50))       # 12586269025
print(my_python_module.fast_sum([1.0, 2.0, 3.0, 4.0, 5.0]))  # 15.0

# Word count
counts = my_python_module.word_count("hello world hello rust hello")
print(counts)  # {'hello': 3, 'world': 1, 'rust': 1}

# Use Rust class
calc = my_python_module.RustCalculator()
print(calc.add(3, 4))        # 7.0
print(calc.multiply(5, 6))   # 30.0
print(calc.get_history())    # [7.0, 30.0]

# Performance comparison
import time

# Python fibonacci
def py_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Benchmark
start = time.time()
for _ in range(100000):
    py_fib(50)
py_time = time.time() - start

start = time.time()
for _ in range(100000):
    my_python_module.fibonacci(50)
rust_time = time.time() - start

print(f"Python: {py_time:.3f}s")
print(f"Rust:   {rust_time:.3f}s")
print(f"Speedup: {py_time/rust_time:.1f}x")
# Typically 10-100x faster!
```

### 7.4 JavaScript / Node.js Interop

```rust
// ═══════════════════════════════════════
// WASM for Browser JavaScript
// ═══════════════════════════════════════
use wasm_bindgen::prelude::*;

// Import JavaScript functions
#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);

    #[wasm_bindgen(js_namespace = Math)]
    fn random() -> f64;

    fn alert(s: &str);
}

// Export Rust functions to JavaScript
#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    log(&format!("greet() called with: {}", name));
    format!("Hello, {}!", name)
}

#[wasm_bindgen]
pub struct ImageProcessor {
    width: u32,
    height: u32,
    pixels: Vec<u8>,
}

#[wasm_bindgen]
impl ImageProcessor {
    #[wasm_bindgen(constructor)]
    pub fn new(width: u32, height: u32) -> ImageProcessor {
        ImageProcessor {
            width,
            height,
            pixels: vec![0; (width * height * 4) as usize],
        }
    }

    pub fn pixels(&self) -> *const u8 {
        self.pixels.as_ptr()
    }

    pub fn grayscale(&mut self) {
        for chunk in self.pixels.chunks_exact_mut(4) {
            let avg = ((chunk[0] as u16 + chunk[1] as u16 + chunk[2] as u16) / 3) as u8;
            chunk[0] = avg;  // R
            chunk[1] = avg;  // G
            chunk[2] = avg;  // B
            // chunk[3] = alpha (unchanged)
        }
    }

    pub fn invert(&mut self) {
        for chunk in self.pixels.chunks_exact_mut(4) {
            chunk[0] = 255 - chunk[0];
            chunk[1] = 255 - chunk[1];
            chunk[2] = 255 - chunk[2];
        }
    }

    pub fn brightness(&mut self, factor: f32) {
        for chunk in self.pixels.chunks_exact_mut(4) {
            chunk[0] = ((chunk[0] as f32 * factor).min(255.0)) as u8;
            chunk[1] = ((chunk[1] as f32 * factor).min(255.0)) as u8;
            chunk[2] = ((chunk[2] as f32 * factor).min(255.0)) as u8;
        }
    }
}
```

```javascript
// Using Rust WASM from JavaScript
import init, { greet, ImageProcessor } from './pkg/my_wasm.js';

async function main() {
    await init();

    // Call Rust function
    const message = greet("World");
    console.log(message);  // "Hello, World!"

    // Use Rust class
    const processor = new ImageProcessor(800, 600);
    processor.grayscale();
    processor.invert();
    processor.brightness(1.5);
}

main();
```

```rust
// ═══════════════════════════════════════
// NAPI-RS for Node.js Native Addon
// ═══════════════════════════════════════
// Cargo.toml:
// [dependencies]
// napi = "2"
// napi-derive = "2"
//
// [lib]
// crate-type = ["cdylib"]

use napi_derive::napi;

#[napi]
pub fn sum(a: i32, b: i32) -> i32 {
    a + b
}

#[napi]
pub fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a: u64 = 0;
            let mut b: u64 = 1;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

#[napi(object)]
pub struct Config {
    pub name: String,
    pub value: i32,
}

#[napi]
pub fn process_config(config: Config) -> String {
    format!("Processing: {} = {}", config.name, config.value)
}
```

```javascript
// Using in Node.js
const { sum, fibonacci, processConfig } = require('./index.node');

console.log(sum(3, 4));           // 7
console.log(fibonacci(50));        // 12586269025n (BigInt)
console.log(processConfig({ name: 'timeout', value: 30 }));
```

### 7.5 Java / Kotlin / Android Interop

```rust
// ═══════════════════════════════════════
// JNI (Java Native Interface)
// ═══════════════════════════════════════
// Cargo.toml:
// [dependencies]
// jni = "0.21"
//
// [lib]
// crate-type = ["cdylib"]

use jni::JNIEnv;
use jni::objects::{JClass, JString};
use jni::sys::{jint, jlong, jstring};

#[no_mangle]
pub extern "system" fn Java_com_example_RustBridge_add(
    _env: JNIEnv,
    _class: JClass,
    a: jint,
    b: jint,
) -> jint {
    a + b
}

#[no_mangle]
pub extern "system" fn Java_com_example_RustBridge_processString(
    mut env: JNIEnv,
    _class: JClass,
    input: JString,
) -> jstring {
    let input: String = env.get_string(&input).unwrap().into();
    let output = format!("Rust processed: {}", input.to_uppercase());
    
    env.new_string(output).unwrap().into_raw()
}

#[no_mangle]
pub extern "system" fn Java_com_example_RustBridge_fibonacci(
    _env: JNIEnv,
    _class: JClass,
    n: jint,
) -> jlong {
    let mut a: i64 = 0;
    let mut b: i64 = 1;
    for _ in 0..n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    a
}
```

```java
// Java side
package com.example;

public class RustBridge {
    static {
        System.loadLibrary("my_rust_lib");
    }

    public static native int add(int a, int b);
    public static native String processString(String input);
    public static native long fibonacci(int n);

    public static void main(String[] args) {
        System.out.println("add(3, 4) = " + add(3, 4));
        System.out.println(processString("hello"));
        System.out.println("fib(50) = " + fibonacci(50));
    }
}
```

```kotlin
// Kotlin / Android side
class RustBridge {
    companion object {
        init {
            System.loadLibrary("my_rust_lib")
        }
    }

    external fun add(a: Int, b: Int): Int
    external fun processString(input: String): String
    external fun fibonacci(n: Int): Long
}

// Usage
val bridge = RustBridge()
println(bridge.add(3, 4))                    // 7
println(bridge.processString("hello"))        // "Rust processed: HELLO"
println(bridge.fibonacci(50))                 // 12586269025
```

### 7.6 UniFFI (Mozilla's Universal FFI)

```rust
// ═══════════════════════════════════════
// UniFFI — One Rust library, multiple language bindings
// Generates: Kotlin, Swift, Python, Ruby bindings automatically!
// ═══════════════════════════════════════

// Cargo.toml:
// [dependencies]
// uniffi = "0.25"
//
// [build-dependencies]
// uniffi = { version = "0.25", features = ["build"] }

// src/lib.rs
uniffi::setup_scaffolding!();

#[derive(uniffi::Record)]
pub struct TodoItem {
    pub id: u64,
    pub title: String,
    pub completed: bool,
}

#[derive(uniffi::Enum)]
pub enum Priority {
    Low,
    Medium,
    High,
}

#[derive(uniffi::Object)]
pub struct TodoList {
    items: std::sync::Mutex<Vec<TodoItem>>,
    next_id: std::sync::Mutex<u64>,
}

#[uniffi::export]
impl TodoList {
    #[uniffi::constructor]
    fn new() -> Self {
        TodoList {
            items: std::sync::Mutex::new(Vec::new()),
            next_id: std::sync::Mutex::new(1),
        }
    }

    fn add_item(&self, title: String) -> u64 {
        let mut id_lock = self.next_id.lock().unwrap();
        let id = *id_lock;
        *id_lock += 1;

        let item = TodoItem {
            id,
            title,
            completed: false,
        };

        self.items.lock().unwrap().push(item);
        id
    }

    fn complete_item(&self, id: u64) -> bool {
        let mut items = self.items.lock().unwrap();
        if let Some(item) = items.iter_mut().find(|i| i.id == id) {
            item.completed = true;
            true
        } else {
            false
        }
    }

    fn get_items(&self) -> Vec<TodoItem> {
        self.items.lock().unwrap().clone()
    }

    fn pending_count(&self) -> u64 {
        self.items.lock().unwrap()
            .iter()
            .filter(|i| !i.completed)
            .count() as u64
    }
}

// This generates bindings for:
// ✅ Kotlin (Android)
// ✅ Swift (iOS)
// ✅ Python
// ✅ Ruby
```

```swift
// Auto-generated Swift usage
let todoList = TodoList()
let id = todoList.addItem(title: "Buy groceries")
todoList.completeItem(id: id)
let items = todoList.getItems()
print("Pending: \(todoList.pendingCount())")
```

```kotlin
// Auto-generated Kotlin usage
val todoList = TodoList()
val id = todoList.addItem("Buy groceries")
todoList.completeItem(id)
val items = todoList.getItems()
println("Pending: ${todoList.pendingCount()}")
```

### 7.7 Network Communication (HTTP, gRPC, WebSocket)

```rust
// ═══════════════════════════════════════
// HTTP CLIENT (reqwest)
// ═══════════════════════════════════════
use reqwest;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct Post {
    #[serde(skip_serializing_if = "Option::is_none")]
    id: Option<u32>,
    title: String,
    body: String,
    #[serde(rename = "userId")]
    user_id: u32,
}

async fn http_examples() -> Result<(), Box<dyn std::error::Error>> {
    let client = reqwest::Client::new();

    // GET request
    let response = client
        .get("https://jsonplaceholder.typicode.com/posts/1")
        .header("Accept", "application/json")
        .send()
        .await?;

    let post: Post = response.json().await?;
    println!("Title: {}", post.title);

    // POST request
    let new_post = Post {
        id: None,
        title: "My Post".to_string(),
        body: "Hello from Rust!".to_string(),
        user_id: 1,
    };

    let response = client
        .post("https://jsonplaceholder.typicode.com/posts")
        .json(&new_post)
        .send()
        .await?;

    println!("Status: {}", response.status());
    let created: Post = response.json().await?;
    println!("Created post with id: {:?}", created.id);

    // Download file
    let bytes = client
        .get("https://example.com/image.png")
        .send()
        .await?
        .bytes()
        .await?;
    std::fs::write("downloaded.png", bytes)?;

    Ok(())
}

// ═══════════════════════════════════════
// HTTP SERVER (axum)
// ═══════════════════════════════════════
use axum::{
    routing::{get, post},
    Router, Json, extract::Path,
    http::StatusCode,
};

#[derive(Serialize)]
struct ApiResponse {
    message: String,
    status: String,
}

async fn hello() -> Json<ApiResponse> {
    Json(ApiResponse {
        message: "Hello from Rust!".to_string(),
        status: "ok".to_string(),
    })
}

async fn get_user(Path(id): Path<u32>) -> Json<serde_json::Value> {
    Json(serde_json::json!({
        "id": id,
        "name": "Alice",
        "email": "alice@example.com"
    }))
}

async fn create_user(Json(payload): Json<serde_json::Value>) -> (StatusCode, Json<serde_json::Value>) {
    (StatusCode::CREATED, Json(serde_json::json!({
        "message": "User created",
        "data": payload
    })))
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(hello))
        .route("/users/:id", get(get_user))
        .route("/users", post(create_user));

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    println!("Server running on http://localhost:3000");
    axum::serve(listener, app).await.unwrap();
}
```

```rust
// ═══════════════════════════════════════
// gRPC (tonic)
// ═══════════════════════════════════════

// proto/hello.proto
// syntax = "proto3";
// package hello;
// 
// service Greeter {
//     rpc SayHello (HelloRequest) returns (HelloReply);
// }
// 
// message HelloRequest {
//     string name = 1;
// }
// 
// message HelloReply {
//     string message = 1;
// }

// build.rs
// fn main() {
//     tonic_build::compile_protos("proto/hello.proto").unwrap();
// }

use tonic::{transport::Server, Request, Response, Status};

pub mod hello {
    tonic::include_proto!("hello");
}

use hello::greeter_server::{Greeter, GreeterServer};
use hello::{HelloReply, HelloRequest};

#[derive(Default)]
pub struct MyGreeter {}

#[tonic::async_trait]
impl Greeter for MyGreeter {
    async fn say_hello(
        &self,
        request: Request<HelloRequest>,
    ) -> Result<Response<HelloReply>, Status> {
        let name = request.into_inner().name;
        let reply = HelloReply {
            message: format!("Hello, {}!", name),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "0.0.0.0:50051".parse()?;
    let greeter = MyGreeter::default();

    println!("gRPC server listening on {}", addr);
    Server::builder()
        .add_service(GreeterServer::new(greeter))
        .serve(addr)
        .await?;

    Ok(())
}
```

### 7.8 Process Communication (Running External Tools)

```rust
use std::process::{Command, Stdio};
use std::io::{Write, BufRead, BufReader};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // ═══════════════════════════════════════
    // RUN EXTERNAL COMMAND
    // ═══════════════════════════════════════

    // Simple command
    let output = Command::new("echo")
        .arg("Hello from external!")
        .output()?;
    println!("Output: {}", String::from_utf8_lossy(&output.stdout));

    // Command with multiple args
    let output = Command::new("ls")
        .args(["-la", "/tmp"])
        .output()?;
    println!("{}", String::from_utf8_lossy(&output.stdout));

    // Check exit status
    let status = Command::new("test")
        .args(["-f", "/etc/hosts"])
        .status()?;
    println!("File exists: {}", status.success());

    // ═══════════════════════════════════════
    // PIPE — Send data to external command
    // ═══════════════════════════════════════

    let mut child = Command::new("sort")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .spawn()?;

    // Write to stdin
    if let Some(mut stdin) = child.stdin.take() {
        stdin.write_all(b"banana\napple\ncherry\ndate\n")?;
    }

    let output = child.wait_with_output()?;
    println!("Sorted:\n{}", String::from_utf8_lossy(&output.stdout));

    // ═══════════════════════════════════════
    // PIPE CHAIN — command1 | command2
    // ═══════════════════════════════════════

    let echo = Command::new("echo")
        .arg("Hello World Hello Rust Hello World")
        .stdout(Stdio::piped())
        .spawn()?;

    let tr = Command::new("tr")
        .args([" ", "\n"])
        .stdin(echo.stdout.unwrap())
        .stdout(Stdio::piped())
        .spawn()?;

    let sort = Command::new("sort")
        .stdin(tr.stdout.unwrap())
        .stdout(Stdio::piped())
        .spawn()?;

    let uniq = Command::new("uniq")
        .args(["-c"])
        .stdin(sort.stdout.unwrap())
        .output()?;

    println!("Word count:\n{}", String::from_utf8_lossy(&uniq.stdout));

    // ═══════════════════════════════════════
    // STREAMING OUTPUT (real-time)
    // ═══════════════════════════════════════

    let mut child = Command::new("ping")
        .args(["-c", "4", "google.com"])
        .stdout(Stdio::piped())
        .spawn()?;

    if let Some(stdout) = child.stdout.take() {
        let reader = BufReader::new(stdout);
        for line in reader.lines() {
            println!("PING: {}", line?);
        }
    }

    child.wait()?;

    // ═══════════════════════════════════════
    // ENVIRONMENT VARIABLES
    // ═══════════════════════════════════════

    let output = Command::new("env")
        .env("MY_VAR", "my_value")
        .env("RUST_APP", "true")
        .env_remove("UNNECESSARY_VAR")
        .current_dir("/tmp")
        .output()?;

    // ═══════════════════════════════════════
    // CALLING COMMON TOOLS
    // ═══════════════════════════════════════

    // Git
    let output = Command::new("git")
        .args(["log", "--oneline", "-5"])
        .output()?;
    println!("Git log:\n{}", String::from_utf8_lossy(&output.stdout));

    // Docker
    let output = Command::new("docker")
        .args(["ps", "--format", "table {{.Names}}\t{{.Status}}"])
        .output()?;
    println!("Docker:\n{}", String::from_utf8_lossy(&output.stdout));

    // curl
    let output = Command::new("curl")
        .args(["-s", "https://httpbin.org/get"])
        .output()?;
    println!("API:\n{}", String::from_utf8_lossy(&output.stdout));

    // Python script
    let output = Command::new("python3")
        .args(["-c", "print(sum(range(100)))"])
        .output()?;
    println!("Python: {}", String::from_utf8_lossy(&output.stdout));

    // Database CLI
    let output = Command::new("psql")
        .args(["-h", "localhost", "-U", "postgres", "-c", "SELECT version();"])
        .env("PGPASSWORD", "mypassword")
        .output()?;

    Ok(())
}
```

### 7.9 Database Communication

```rust
// ═══════════════════════════════════════
// SQLx — Async SQL with compile-time checked queries
// ═══════════════════════════════════════
use sqlx::{postgres::PgPoolOptions, FromRow, Row};

#[derive(Debug, FromRow)]
struct User {
    id: i64,
    username: String,
    email: String,
    created_at: chrono::NaiveDateTime,
}

#[tokio::main]
async fn main() -> Result<(), sqlx::Error> {
    // Connect to PostgreSQL
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect("postgres://user:pass@localhost/mydb")
        .await?;

    // Create table
    sqlx::query(
        "CREATE TABLE IF NOT EXISTS users (
            id BIGSERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        )"
    )
    .execute(&pool)
    .await?;

    // Insert
    let result = sqlx::query(
        "INSERT INTO users (username, email) VALUES ($1, $2) RETURNING id"
    )
    .bind("alice")
    .bind("alice@example.com")
    .fetch_one(&pool)
    .await?;
    
    let id: i64 = result.get("id");
    println!("Inserted user with id: {}", id);

    // Query single row
    let user = sqlx::query_as::<_, User>(
        "SELECT * FROM users WHERE username = $1"
    )
    .bind("alice")
    .fetch_optional(&pool)
    .await?;

    if let Some(user) = user {
        println!("Found: {:?}", user);
    }

    // Query multiple rows
    let users = sqlx::query_as::<_, User>(
        "SELECT * FROM users ORDER BY created_at DESC LIMIT 10"
    )
    .fetch_all(&pool)
    .await?;

    for user in &users {
        println!("{}: {} ({})", user.id, user.username, user.email);
    }

    // Compile-time checked queries (with sqlx::query! macro)
    // Requires DATABASE_URL environment variable
    // let user = sqlx::query!("SELECT * FROM users WHERE id = $1", 1i64)
    //     .fetch_one(&pool)
    //     .await?;
    // println!("{}", user.username);

    Ok(())
}
```

```rust
// ═══════════════════════════════════════
// Redis
// ═══════════════════════════════════════
use redis::AsyncCommands;

#[tokio::main]
async fn main() -> redis::RedisResult<()> {
    let client = redis::Client::open("redis://127.0.0.1/")?;
    let mut con = client.get_async_connection().await?;

    // Set/Get
    con.set("key", "value").await?;
    let val: String = con.get("key").await?;
    println!("Value: {}", val);

    // Hash
    con.hset("user:1", "name", "Alice").await?;
    con.hset("user:1", "age", 30).await?;
    let name: String = con.hget("user:1", "name").await?;
    println!("Name: {}", name);

    // List
    con.rpush("queue", "task1").await?;
    con.rpush("queue", "task2").await?;
    let task: String = con.lpop("queue", None).await?;
    println!("Task: {}", task);

    // Expiration
    con.set_ex("temp_key", "expires soon", 60).await?;

    Ok(())
}
```

### 7.10 Complete Communication Methods Summary

```
╔══════════════════════════════════════════════════════════════════════╗
║              ALL COMMUNICATION METHODS                              ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  METHOD              │ USE CASE                │ CRATE / TOOL        ║
║  ────────────────────┼─────────────────────────┼──────────────────── ║
║                                                                      ║
║  ── LANGUAGE INTEROP ──                                              ║
║  C FFI (extern "C")  │ Call C / Be called by C │ libc, bindgen, cc   ║
║  C++ FFI             │ Call C++ libraries       │ cxx, autocxx        ║
║  Python bindings     │ Python extension modules │ PyO3, maturin       ║
║  Node.js bindings    │ Node native addons       │ napi-rs, neon       ║
║  Java/Kotlin (JNI)   │ Android, Java apps       │ jni crate           ║
║  Swift/ObjC          │ iOS/macOS integration    │ UniFFI, swift-rs     ║
║  Ruby bindings       │ Ruby gems                │ magnus, UniFFI       ║
║  WASM                │ Browser JavaScript       │ wasm-bindgen         ║
║  UniFFI              │ Multi-language at once   │ uniffi               ║
║                                                                      ║
║  ── NETWORK PROTOCOLS ──                                             ║
║  HTTP/HTTPS          │ REST APIs, web           │ reqwest, hyper, axum ║
║  gRPC                │ Microservices            │ tonic                ║
║  WebSocket           │ Real-time communication  │ tokio-tungstenite    ║
║  GraphQL             │ Flexible APIs            │ async-graphql, juniper║
║  MQTT                │ IoT messaging            │ rumqttc              ║
║  AMQP                │ Message queues           │ lapin                ║
║  TCP/UDP raw         │ Custom protocols         │ std::net, tokio::net ║
║  Unix sockets        │ Local IPC                │ tokio::net::UnixStream║
║                                                                      ║
║  ── DATABASES ──                                                     ║
║  PostgreSQL          │ Relational DB            │ sqlx, diesel, tokio-postgres ║
║  MySQL               │ Relational DB            │ sqlx, diesel         ║
║  SQLite              │ Embedded DB              │ sqlx, rusqlite       ║
║  Redis               │ Cache / Key-Value        │ redis                ║
║  MongoDB             │ Document DB              │ mongodb              ║
║  Elasticsearch       │ Search engine            │ elasticsearch        ║
║  DynamoDB            │ AWS NoSQL                │ aws-sdk-dynamodb     ║
║  Cassandra           │ Wide-column DB           │ scylla               ║
║                                                                      ║
║  ── MESSAGE QUEUES ──                                                ║
║  Kafka               │ Event streaming          │ rdkafka              ║
║  RabbitMQ            │ Message broker           │ lapin                ║
║  NATS                │ Cloud messaging          │ nats                 ║
║  ZeroMQ              │ Distributed messaging    │ zmq                  ║
║                                                                      ║
║  ── PROCESS / OS ──                                                  ║
║  Process spawn       │ Run external commands    │ std::process::Command║
║  Pipes               │ stdin/stdout/stderr      │ std::process::Stdio  ║
║  Shared memory       │ Inter-process comm       │ shared_memory        ║
║  Signals             │ Unix signals             │ signal-hook, ctrlc   ║
║  D-Bus               │ Linux desktop IPC        │ zbus                 ║
║  Named pipes/FIFO    │ IPC                      │ std::fs, nix         ║
║  Memory-mapped files │ Shared data              │ memmap2              ║
║                                                                      ║
║  ── FILE FORMATS ──                                                  ║
║  JSON                │ Data interchange         │ serde_json           ║
║  YAML                │ Configuration            │ serde_yaml           ║
║  TOML                │ Configuration            │ toml                 ║
║  XML                 │ Legacy data              │ quick-xml            ║
║  CSV                 │ Tabular data             │ csv                  ║
║  Protobuf            │ Binary serialization     │ prost                ║
║  MessagePack         │ Binary JSON-like         │ rmp-serde            ║
║  Parquet             │ Columnar data            │ parquet              ║
║  Avro                │ Schema evolution         │ apache-avro          ║
║                                                                      ║
║  ── CLOUD SERVICES ──                                                ║
║  AWS SDK             │ All AWS services         │ aws-sdk-*            ║
║  GCP                 │ Google Cloud services    │ google-cloud-*       ║
║  Azure               │ Azure services           │ azure_*              ║
║                                                                      ║
║  ── HARDWARE INTERFACES ──                                           ║
║  Serial (UART)       │ Microcontrollers         │ serialport           ║
║  USB                 │ USB devices              │ rusb, nusb           ║
║  Bluetooth           │ BLE devices              │ btleplug             ║
║  GPIO                │ Raspberry Pi pins        │ rppal, gpio-cdev     ║
║  I2C                 │ Sensors, displays        │ linux-embedded-hal   ║
║  SPI                 │ High-speed peripherals   │ linux-embedded-hal   ║
║  CAN bus             │ Automotive               │ socketcan            ║
║  MIDI                │ Musical instruments      │ midir                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## PART 8: HARDWARE INTERFACE EXAMPLES

### 8.1 Serial Port (UART)

```rust
// Cargo.toml: serialport = "4.3"

use serialport;
use std::time::Duration;
use std::io::{Read, Write};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // List available ports
    let ports = serialport::available_ports()?;
    for port in &ports {
        println!("Found port: {}", port.port_name);
    }

    // Open serial port
    let mut port = serialport::new("/dev/ttyUSB0", 9600)
        .timeout(Duration::from_millis(1000))
        .data_bits(serialport::DataBits::Eight)
        .parity(serialport::Parity::None)
        .stop_bits(serialport::StopBits::One)
        .flow_control(serialport::FlowControl::None)
        .open()?;

    // Write data
    port.write_all(b"Hello Arduino!\n")?;

    // Read response
    let mut buffer = [0u8; 256];
    loop {
        match port.read(&mut buffer) {
            Ok(bytes_read) => {
                let data = String::from_utf8_lossy(&buffer[..bytes_read]);
                print!("Received: {}", data);
            }
            Err(ref e) if e.kind() == std::io::ErrorKind::TimedOut => {
                // No data available, continue
            }
            Err(e) => {
                eprintln!("Error: {}", e);
                break;
            }
        }
    }

    Ok(())
}
```

### 8.2 GPIO (Raspberry Pi)

```rust
// Cargo.toml: rppal = "0.17"

use rppal::gpio::Gpio;
use std::thread;
use std::time::Duration;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let gpio = Gpio::new()?;

    // LED on GPIO pin 17
    let mut led = gpio.get(17)?.into_output();

    // Button on GPIO pin 27
    let button = gpio.get(27)?.into_input_pullup();

    println!("Blinking LED...");

    // Blink LED
    for _ in 0..10 {
        led.set_high();
        thread::sleep(Duration::from_millis(500));
        led.set_low();
        thread::sleep(Duration::from_millis(500));
    }

    // React to button press
    println!("Waiting for button press...");
    loop {
        if button.is_low() {
            println!("Button pressed!");
            led.set_high();
        } else {
            led.set_low();
        }
        thread::sleep(Duration::from_millis(10));
    }
}
```

### 8.3 USB Devices

```rust
// Cargo.toml: rusb = "0.9"

use rusb;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // List all USB devices
    for device in rusb::devices()?.iter() {
        let desc = device.device_descriptor()?;
        println!(
            "Bus {:03} Device {:03} ID {:04x}:{:04x}",
            device.bus_number(),
            device.address(),
            desc.vendor_id(),
            desc.product_id()
        );

        // Get manufacturer and product strings
        if let Ok(handle) = device.open() {
            if let Ok(manufacturer) = handle.read_manufacturer_string_ascii(&desc) {
                println!("  Manufacturer: {}", manufacturer);
            }
            if let Ok(product) = handle.read_product_string_ascii(&desc) {
                println!("  Product: {}", product);
            }
        }
    }

    Ok(())
}
```

### 8.4 Bluetooth Low Energy (BLE)

```rust
// Cargo.toml: btleplug = "0.11"

use btleplug::api::{Central, Manager as _, Peripheral as _, ScanFilter};
use btleplug::platform::Manager;
use std::time::Duration;
use tokio;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let manager = Manager::new().await?;
    let adapters = manager.adapters().await?;
    let adapter = adapters.into_iter().next().unwrap();

    println!("Scanning for BLE devices...");
    adapter.start_scan(ScanFilter::default()).await?;
    tokio::time::sleep(Duration::from_secs(5)).await;

    let peripherals = adapter.peripherals().await?;
    for peripheral in peripherals {
        let properties = peripheral.properties().await?;
        if let Some(props) = properties {
            println!(
                "Device: {} (RSSI: {:?})",
                props.local_name.unwrap_or("Unknown".to_

# 🦀 Rust Hardware Guide (Continued)

---

## PART 8: HARDWARE INTERFACE EXAMPLES (Continued)

### 8.4 Bluetooth Low Energy (Continued)

```rust
// Cargo.toml: btleplug = "0.11", tokio = { version = "1", features = ["full"] }

use btleplug::api::{Central, Manager as _, Peripheral as _, ScanFilter, WriteType};
use btleplug::platform::Manager;
use std::time::Duration;
use tokio;
use uuid::Uuid;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize BLE
    let manager = Manager::new().await?;
    let adapters = manager.adapters().await?;
    let adapter = adapters.into_iter().next()
        .ok_or("No Bluetooth adapter found")?;

    println!("Scanning for BLE devices...");
    adapter.start_scan(ScanFilter::default()).await?;
    tokio::time::sleep(Duration::from_secs(5)).await;

    // List discovered devices
    let peripherals = adapter.peripherals().await?;
    for peripheral in &peripherals {
        let properties = peripheral.properties().await?;
        if let Some(props) = properties {
            let name = props.local_name.unwrap_or("Unknown".to_string());
            let rssi = props.rssi.unwrap_or(0);
            let address = props.address;
            println!("Device: {} | Address: {} | RSSI: {} dBm", name, address, rssi);
        }
    }

    // Connect to a specific device
    for peripheral in &peripherals {
        let props = peripheral.properties().await?;
        if let Some(props) = props {
            if props.local_name.as_deref() == Some("MyDevice") {
                println!("Connecting to MyDevice...");
                peripheral.connect().await?;
                println!("Connected!");

                // Discover services
                peripheral.discover_services().await?;
                let services = peripheral.services();
                for service in &services {
                    println!("Service: {}", service.uuid);
                    for characteristic in &service.characteristics {
                        println!("  Characteristic: {}", characteristic.uuid);
                        println!("  Properties: {:?}", characteristic.properties);
                    }
                }

                // Read a characteristic
                let target_uuid = Uuid::parse_str("0000180f-0000-1000-8000-00805f9b34fb")?;
                for service in &services {
                    for char in &service.characteristics {
                        if char.uuid == target_uuid {
                            let value = peripheral.read(&char).await?;
                            println!("Read value: {:?}", value);
                        }
                    }
                }

                // Write to a characteristic
                // peripheral.write(&characteristic, &[0x01, 0x02], WriteType::WithResponse).await?;

                // Subscribe to notifications
                // peripheral.subscribe(&characteristic).await?;
                // let mut notification_stream = peripheral.notifications().await?;
                // while let Some(notification) = notification_stream.next().await {
                //     println!("Notification: {:?}", notification.value);
                // }

                peripheral.disconnect().await?;
                println!("Disconnected.");
                break;
            }
        }
    }

    Ok(())
}
```

### 8.5 I2C Communication (Sensors)

```rust
// ═══════════════════════════════════════
// I2C on Raspberry Pi (reading temperature sensor)
// Cargo.toml: rppal = "0.17"
// ═══════════════════════════════════════

use rppal::i2c::I2c;
use std::thread;
use std::time::Duration;

// BME280 Temperature/Humidity/Pressure Sensor
const BME280_ADDR: u16 = 0x76;
const REG_TEMP_MSB: u8 = 0xFA;
const REG_CHIP_ID: u8 = 0xD0;
const REG_CTRL_MEAS: u8 = 0xF4;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut i2c = I2c::new()?;

    // Set slave address
    i2c.set_slave_address(BME280_ADDR)?;

    // Read chip ID
    let mut chip_id = [0u8; 1];
    i2c.block_read(REG_CHIP_ID, &mut chip_id)?;
    println!("Chip ID: 0x{:02X}", chip_id[0]);

    // Configure sensor (temperature oversampling x1, normal mode)
    i2c.block_write(REG_CTRL_MEAS, &[0x27])?;
    thread::sleep(Duration::from_millis(100));

    // Read temperature
    loop {
        let mut temp_data = [0u8; 3];
        i2c.block_read(REG_TEMP_MSB, &mut temp_data)?;

        let raw_temp = ((temp_data[0] as i32) << 12)
            | ((temp_data[1] as i32) << 4)
            | ((temp_data[2] as i32) >> 4);

        // Simplified conversion (real code needs calibration data)
        let temperature = raw_temp as f64 / 5120.0;
        println!("Temperature: {:.1}°C", temperature);

        thread::sleep(Duration::from_secs(2));
    }
}

// ═══════════════════════════════════════
// I2C on Embedded (no_std) — using embedded-hal
// ═══════════════════════════════════════

// This works on ANY microcontroller that implements embedded-hal
use embedded_hal::i2c::I2c as I2cTrait;

struct TemperatureSensor<I2C> {
    i2c: I2C,
    address: u8,
}

impl<I2C: I2cTrait> TemperatureSensor<I2C> {
    pub fn new(i2c: I2C, address: u8) -> Self {
        Self { i2c, address }
    }

    pub fn read_temperature(&mut self) -> Result<f32, I2C::Error> {
        let mut buf = [0u8; 2];
        self.i2c.write_read(self.address, &[0xFA], &mut buf)?;

        let raw = ((buf[0] as u16) << 8) | (buf[1] as u16);
        let temp = raw as f32 * 0.0625;
        Ok(temp)
    }

    pub fn read_chip_id(&mut self) -> Result<u8, I2C::Error> {
        let mut buf = [0u8; 1];
        self.i2c.write_read(self.address, &[0xD0], &mut buf)?;
        Ok(buf[0])
    }
}
```

### 8.6 SPI Communication

```rust
// ═══════════════════════════════════════
// SPI on Raspberry Pi
// Cargo.toml: rppal = "0.17"
// ═══════════════════════════════════════

use rppal::spi::{Bus, Mode, SlaveSelect, Spi};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Open SPI bus 0, chip select 0
    let mut spi = Spi::new(
        Bus::Spi0,
        SlaveSelect::Ss0,
        1_000_000,      // 1 MHz clock speed
        Mode::Mode0,     // CPOL=0, CPHA=0
    )?;

    // Transfer data (simultaneous read/write)
    let tx_buf = [0x9F, 0x00, 0x00, 0x00]; // Read JEDEC ID command
    let mut rx_buf = [0u8; 4];
    spi.transfer(&mut rx_buf, &tx_buf)?;

    println!("SPI Response: {:02X?}", rx_buf);
    println!("Manufacturer: 0x{:02X}", rx_buf[1]);
    println!("Device ID: 0x{:02X}{:02X}", rx_buf[2], rx_buf[3]);

    // Write only
    spi.write(&[0x06])?;   // Write enable command

    // Read only
    let mut read_buf = [0u8; 4];
    spi.read(&mut read_buf)?;
    println!("Read: {:02X?}", read_buf);

    Ok(())
}
```

### 8.7 PWM (Motor/LED Control)

```rust
// ═══════════════════════════════════════
// PWM on Raspberry Pi
// Cargo.toml: rppal = "0.17"
// ═══════════════════════════════════════

use rppal::pwm::{Channel, Polarity, Pwm};
use std::thread;
use std::time::Duration;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize PWM on channel 0 (GPIO 18)
    let pwm = Pwm::with_frequency(
        Channel::Pwm0,
        50.0,              // 50 Hz (standard for servos)
        0.075,             // 7.5% duty cycle (center position)
        Polarity::Normal,
        true,              // enabled
    )?;

    println!("Servo control demo...");

    // Sweep servo from 0° to 180°
    // 0° = 2.5% duty, 90° = 7.5% duty, 180° = 12.5% duty
    for angle in (0..=180).step_by(10) {
        let duty = 0.025 + (angle as f64 / 180.0) * 0.1;
        pwm.set_duty_cycle(duty)?;
        println!("Angle: {}° | Duty: {:.1}%", angle, duty * 100.0);
        thread::sleep(Duration::from_millis(200));
    }

    // LED brightness control (fade in/out)
    let led_pwm = Pwm::with_frequency(
        Channel::Pwm1,    // GPIO 19
        1000.0,            // 1 kHz for LEDs
        0.0,               // start at 0% (off)
        Polarity::Normal,
        true,
    )?;

    println!("LED fade demo...");
    loop {
        // Fade in
        for i in 0..=100 {
            led_pwm.set_duty_cycle(i as f64 / 100.0)?;
            thread::sleep(Duration::from_millis(10));
        }
        // Fade out
        for i in (0..=100).rev() {
            led_pwm.set_duty_cycle(i as f64 / 100.0)?;
            thread::sleep(Duration::from_millis(10));
        }
    }
}
```

### 8.8 Camera / Video Capture

```rust
// ═══════════════════════════════════════
// Camera capture using OpenCV bindings
// Cargo.toml: opencv = { version = "0.88", features = ["videoio", "highgui"] }
// ═══════════════════════════════════════

use opencv::{
    core,
    highgui,
    prelude::*,
    videoio,
};

fn main() -> opencv::Result<()> {
    // Open default camera
    let mut camera = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;
    if !camera.is_opened()? {
        panic!("Unable to open camera!");
    }

    // Set resolution
    camera.set(videoio::CAP_PROP_FRAME_WIDTH, 640.0)?;
    camera.set(videoio::CAP_PROP_FRAME_HEIGHT, 480.0)?;

    println!("Camera opened. Press 'q' to quit.");

    let mut frame = core::Mat::default();

    loop {
        camera.read(&mut frame)?;
        if frame.empty() {
            continue;
        }

        // Display frame
        highgui::imshow("Camera", &frame)?;

        // Save frame on 's' key press
        let key = highgui::wait_key(1)?;
        if key == 's' as i32 {
            opencv::imgcodecs::imwrite("capture.jpg", &frame, &core::Vector::new())?;
            println!("Frame saved!");
        }
        if key == 'q' as i32 {
            break;
        }
    }

    Ok(())
}
```

### 8.9 Audio

```rust
// ═══════════════════════════════════════
// Audio playback and recording
// Cargo.toml: cpal = "0.15", hound = "3.5"
// ═══════════════════════════════════════

use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
use std::f32::consts::PI;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let host = cpal::default_host();

    // List audio devices
    println!("=== Audio Devices ===");
    for device in host.output_devices()? {
        println!("Output: {}", device.name()?);
    }
    for device in host.input_devices()? {
        println!("Input: {}", device.name()?);
    }

    // Play a sine wave tone
    let device = host.default_output_device()
        .ok_or("No output device")?;
    let config = device.default_output_config()?;

    println!("Playing 440 Hz tone...");

    let sample_rate = config.sample_rate().0 as f32;
    let mut sample_clock = 0f32;
    let frequency = 440.0;  // A4 note

    let stream = device.build_output_stream(
        &config.into(),
        move |data: &mut [f32], _: &cpal::OutputCallbackInfo| {
            for sample in data.iter_mut() {
                let value = (sample_clock * frequency * 2.0 * PI / sample_rate).sin();
                *sample = value * 0.3;  // volume
                sample_clock += 1.0;
            }
        },
        |err| eprintln!("Audio error: {}", err),
        None,
    )?;

    stream.play()?;
    std::thread::sleep(std::time::Duration::from_secs(2));
    drop(stream);

    println!("Done!");
    Ok(())
}
```

```rust
// ═══════════════════════════════════════
// Record audio to WAV file
// ═══════════════════════════════════════

use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
use hound;
use std::sync::{Arc, Mutex};

fn record_audio() -> Result<(), Box<dyn std::error::Error>> {
    let host = cpal::default_host();
    let device = host.default_input_device()
        .ok_or("No input device")?;
    let config = device.default_input_config()?;

    println!("Recording for 5 seconds...");

    let spec = hound::WavSpec {
        channels: config.channels(),
        sample_rate: config.sample_rate().0,
        bits_per_sample: 32,
        sample_format: hound::SampleFormat::Float,
    };

    let writer = Arc::new(Mutex::new(
        hound::WavWriter::create("recording.wav", spec)?
    ));
    let writer_clone = Arc::clone(&writer);

    let stream = device.build_input_stream(
        &config.into(),
        move |data: &[f32], _: &cpal::InputCallbackInfo| {
            let mut writer = writer_clone.lock().unwrap();
            for &sample in data {
                writer.write_sample(sample).ok();
            }
        },
        |err| eprintln!("Error: {}", err),
        None,
    )?;

    stream.play()?;
    std::thread::sleep(std::time::Duration::from_secs(5));
    drop(stream);

    writer.lock().unwrap().finalize()?;
    println!("Saved to recording.wav");

    Ok(())
}
```

---

## PART 9: HARDWARE PERFORMANCE COMPARISON

### 9.1 Rust vs Other Languages on Different Hardware

```
╔══════════════════════════════════════════════════════════════════════╗
║          PERFORMANCE COMPARISON (Approximate)                        ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Task: Matrix multiplication (1000x1000)                             ║
║  Hardware: x86_64 (AMD Ryzen 7)                                      ║
║  ┌───────────┬──────────┬────────────┐                               ║
║  │ Language   │ Time     │ Relative   │                               ║
║  ├───────────┼──────────┼────────────┤                               ║
║  │ C          │ 0.45s    │ 1.0x       │                               ║
║  │ Rust       │ 0.46s    │ 1.02x      │  ← Nearly identical to C    ║
║  │ C++        │ 0.47s    │ 1.04x      │                               ║
║  │ Java       │ 1.2s     │ 2.7x       │                               ║
║  │ Go         │ 1.8s     │ 4.0x       │                               ║
║  │ JavaScript │ 3.5s     │ 7.8x       │                               ║
║  │ Python     │ 45.0s    │ 100x       │                               ║
║  └───────────┴──────────┴────────────┘                               ║
║                                                                      ║
║  Task: HTTP server (requests/second)                                 ║
║  Hardware: x86_64 server                                             ║
║  ┌───────────────────┬──────────────┬────────────┐                   ║
║  │ Framework          │ Req/sec      │ Relative   │                   ║
║  ├───────────────────┼──────────────┼────────────┤                   ║
║  │ Rust (actix-web)   │ 650,000      │ 1.0x       │                   ║
║  │ Rust (axum)        │ 580,000      │ 0.89x      │                   ║
║  │ C++ (drogon)       │ 620,000      │ 0.95x      │                   ║
║  │ Go (fasthttp)      │ 450,000      │ 0.69x      │                   ║
║  │ Java (Spring)      │ 200,000      │ 0.31x      │                   ║
║  │ Node.js (fastify)  │ 120,000      │ 0.18x      │                   ║
║  │ Python (FastAPI)   │ 15,000       │ 0.02x      │                   ║
║  └───────────────────┴──────────────┴────────────┘                   ║
║                                                                      ║
║  Task: Binary size (Hello World)                                     ║
║  ┌───────────────────┬──────────────┐                                ║
║  │ Language/Config     │ Binary Size  │                               ║
║  ├───────────────────┼──────────────┤                                ║
║  │ C (static)         │ 900 KB       │                                ║
║  │ Rust (stripped)     │ 300 KB       │                                ║
║  │ Rust (default)      │ 3.5 MB       │                                ║
║  │ Rust (musl static) │ 1.2 MB       │                                ║
║  │ Go (static)        │ 2.0 MB       │                                ║
║  │ Go (stripped)      │ 1.3 MB       │                                ║
║  └───────────────────┴──────────────┘                                ║
║                                                                      ║
║  Task: Memory usage (web server idle)                                ║
║  ┌───────────────────┬──────────────┐                                ║
║  │ Language            │ RAM Usage    │                               ║
║  ├───────────────────┼──────────────┤                                ║
║  │ Rust               │ 1.5 MB       │                                ║
║  │ C                   │ 1.2 MB       │                                ║
║  │ Go                  │ 8 MB         │                                ║
║  │ Java                │ 50-100 MB    │                                ║
║  │ Node.js             │ 30-50 MB     │                                ║
║  │ Python              │ 20-40 MB     │                                ║
║  └───────────────────┴──────────────┘                                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

### 9.2 Embedded Performance

```
╔══════════════════════════════════════════════════════════════════════╗
║          EMBEDDED PERFORMANCE COMPARISON                             ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Hardware: STM32F4 (ARM Cortex-M4, 168 MHz)                         ║
║                                                                      ║
║  ┌──────────────────────┬──────────┬───────────┬───────────┐        ║
║  │ Metric                │ C        │ Rust      │ C++       │        ║
║  ├──────────────────────┼──────────┼───────────┼───────────┤        ║
║  │ Flash usage (blink)   │ 2.1 KB   │ 2.4 KB    │ 3.2 KB    │        ║
║  │ RAM usage (blink)     │ 32 B     │ 36 B      │ 64 B      │        ║
║  │ GPIO toggle speed     │ 42 MHz   │ 42 MHz    │ 42 MHz    │        ║
║  │ Interrupt latency     │ 12 cycles│ 12 cycles │ 14 cycles │        ║
║  │ Compile time          │ 0.5s     │ 5s        │ 2s        │        ║
║  └──────────────────────┴──────────┴───────────┴───────────┘        ║
║                                                                      ║
║  KEY INSIGHT: Rust produces nearly identical machine code to C       ║
║  with the added benefit of memory safety at ZERO runtime cost.       ║
║                                                                      ║
║  Hardware: ESP32 (Xtensa LX6, 240 MHz)                              ║
║                                                                      ║
║  ┌──────────────────────┬──────────┬───────────┐                    ║
║  │ Metric                │ C (IDF)  │ Rust      │                    ║
║  ├──────────────────────┼──────────┼───────────┤                    ║
║  │ WiFi connect time     │ 2.1s     │ 2.1s      │                    ║
║  │ HTTP request           │ 45ms     │ 47ms      │                    ║
║  │ JSON parse (1KB)      │ 3ms      │ 3ms       │                    ║
║  │ Flash usage (WiFi)    │ 850 KB   │ 920 KB    │                    ║
║  │ Free heap (WiFi)      │ 180 KB   │ 170 KB    │                    ║
║  └──────────────────────┴──────────┴───────────┘                    ║
║                                                                      ║
║  WASM Performance (browser):                                         ║
║                                                                      ║
║  ┌──────────────────────┬──────────┬───────────┐                    ║
║  │ Task                  │ JS       │ Rust WASM │                    ║
║  ├──────────────────────┼──────────┼───────────┤                    ║
║  │ Fibonacci(40)         │ 1200ms   │ 180ms     │  6.7x faster      ║
║  │ Image processing      │ 800ms    │ 95ms      │  8.4x faster      ║
║  │ JSON parse (large)    │ 50ms     │ 15ms      │  3.3x faster      ║
║  │ Sorting (1M items)    │ 450ms    │ 120ms     │  3.8x faster      ║
║  │ Regex matching        │ 200ms    │ 35ms      │  5.7x faster      ║
║  └──────────────────────┴──────────┴───────────┘                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## PART 10: SETTING UP FOR DIFFERENT HARDWARE

### 10.1 Quick Setup Guide Per Platform

```bash
# ══════════════════════════════════════
# DESKTOP (default — just install Rust)
# ══════════════════════════════════════
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
cargo new my_app && cd my_app && cargo run

# ══════════════════════════════════════
# CROSS-COMPILATION SETUP
# ══════════════════════════════════════
cargo install cross           # Docker-based cross compilation
# Now just use `cross` instead of `cargo`:
cross build --target aarch64-unknown-linux-gnu
cross build --target armv7-unknown-linux-gnueabihf
cross build --target x86_64-pc-windows-gnu

# ══════════════════════════════════════
# WEBASSEMBLY SETUP
# ══════════════════════════════════════
rustup target add wasm32-unknown-unknown
cargo install wasm-pack
cargo install trunk

# Create WASM project
cargo new --lib my_wasm && cd my_wasm
# Add to Cargo.toml:
# [lib]
# crate-type = ["cdylib"]
# [dependencies]
# wasm-bindgen = "0.2"
wasm-pack build --target web

# ══════════════════════════════════════
# EMBEDDED ARM (STM32) SETUP
# ══════════════════════════════════════
rustup target add thumbv7em-none-eabihf       # Cortex-M4/M7
rustup target add thumbv7m-none-eabi          # Cortex-M3
rustup target add thumbv6m-none-eabi          # Cortex-M0
cargo install probe-rs --features cli         # Flash & debug tool
cargo install cargo-embed                      # Easier flashing
cargo install cargo-generate                   # Project templates

# Generate embedded project from template
cargo generate --git https://github.com/rust-embedded/cortex-m-quickstart
# OR for STM32:
cargo generate --git https://github.com/stm32-rs/stm32-template

# Build and flash
cargo embed --release

# ══════════════════════════════════════
# EMBEDDED ESP32 SETUP
# ══════════════════════════════════════

# Option 1: std (with operating system features)
cargo install espup
espup install                                 # Install ESP toolchain
cargo install cargo-espflash
cargo install ldproxy

# For ESP32 (Xtensa) — needs special toolchain
cargo generate esp-rs/esp-idf-template cargo
cd my_esp_project
cargo build
cargo espflash flash --monitor

# For ESP32-C3 (RISC-V) — works with standard Rust
rustup target add riscv32imc-unknown-none-elf
cargo generate esp-rs/esp-template
cargo build
cargo espflash flash --monitor

# Option 2: no_std (bare metal, smaller)
cargo generate esp-rs/esp-template
# Select no_std option

# ══════════════════════════════════════
# RASPBERRY PI PICO (RP2040) SETUP
# ══════════════════════════════════════
rustup target add thumbv6m-none-eabi
cargo install elf2uf2-rs                      # Convert to UF2 format
cargo install probe-rs --features cli

# Create project
cargo generate --git https://github.com/rp-rs/rp2040-project-template

# Build
cargo build --release

# Flash (hold BOOTSEL, connect USB, release)
elf2uf2-rs target/thumbv6m-none-eabi/release/my_project
# Drag .uf2 file to RPI-RP2 drive

# OR with probe-rs (with debug probe)
cargo embed --release

# ══════════════════════════════════════
# ANDROID SETUP
# ══════════════════════════════════════
rustup target add aarch64-linux-android
rustup target add armv7-linux-androideabi
rustup target add x86_64-linux-android
rustup target add i686-linux-android
cargo install cargo-ndk

# Build for Android
export ANDROID_NDK_HOME=/path/to/android/ndk
cargo ndk -t arm64-v8a build --release
cargo ndk -t armeabi-v7a build --release

# ══════════════════════════════════════
# iOS SETUP
# ══════════════════════════════════════
rustup target add aarch64-apple-ios
rustup target add aarch64-apple-ios-sim
rustup target add x86_64-apple-ios
cargo install cargo-lipo                      # Universal iOS binaries

cargo lipo --release                          # Build universal library

# ══════════════════════════════════════
# PYTHON EXTENSION SETUP
# ══════════════════════════════════════
pip install maturin
cargo new --lib my_python_ext && cd my_python_ext
# Add to Cargo.toml:
# [lib]
# crate-type = ["cdylib"]
# [dependencies]
# pyo3 = { version = "0.20", features = ["extension-module"] }
maturin develop                               # Build & install in current venv
maturin build --release                       # Build wheel

# ══════════════════════════════════════
# NODE.JS NATIVE ADDON SETUP
# ══════════════════════════════════════
npm install -g @napi-rs/cli
napi new my_node_addon                        # Create project
cd my_node_addon
npm run build                                 # Build addon
```

### 10.2 Platform-Specific Cargo Configuration

```toml
# .cargo/config.toml — Complete example

# ═══ Default target (uncomment one) ═══
# [build]
# target = "thumbv7em-none-eabihf"        # For embedded ARM
# target = "wasm32-unknown-unknown"        # For WASM
# target = "aarch64-unknown-linux-gnu"     # For ARM64 Linux

# ═══ Cross-compilation linkers ═══
[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"

[target.armv7-unknown-linux-gnueabihf]
linker = "arm-linux-gnueabihf-gcc"

[target.x86_64-pc-windows-gnu]
linker = "x86_64-w64-mingw32-gcc"

[target.x86_64-unknown-linux-musl]
linker = "musl-gcc"

# ═══ Embedded ARM ═══
[target.thumbv7em-none-eabihf]
runner = "probe-rs run --chip STM32F411CEUx"
rustflags = [
    "-C", "link-arg=-Tlink.x",        # Memory layout
    "-C", "link-arg=--nmagic",         # No page alignment
]

[target.thumbv6m-none-eabi]
runner = "probe-rs run --chip RP2040"
rustflags = [
    "-C", "link-arg=-Tlink.x",
    "-C", "link-arg=--nmagic",
]

# ═══ WASM ═══
[target.wasm32-unknown-unknown]
runner = "wasm-bindgen-test-runner"

# ═══ Optimization for all targets ═══
[profile.release]
opt-level = 3
lto = true
codegen-units = 1
strip = true

# ═══ Smaller binaries for embedded ═══
[profile.release.package."*"]
opt-level = "s"               # Optimize for size

[profile.dev]
opt-level = 1                  # Some optimization even in debug
```

### 10.3 Conditional Compilation (Platform Detection)

```rust
fn main() {
    // ═══════════════════════════════════════
    // DETECT OPERATING SYSTEM
    // ═══════════════════════════════════════

    #[cfg(target_os = "linux")]
    println!("Running on Linux!");

    #[cfg(target_os = "macos")]
    println!("Running on macOS!");

    #[cfg(target_os = "windows")]
    println!("Running on Windows!");

    #[cfg(target_os = "android")]
    println!("Running on Android!");

    #[cfg(target_os = "ios")]
    println!("Running on iOS!");

    #[cfg(target_os = "none")]
    // Bare metal — no OS!

    // ═══════════════════════════════════════
    // DETECT CPU ARCHITECTURE
    // ═══════════════════════════════════════

    #[cfg(target_arch = "x86_64")]
    println!("x86_64 architecture");

    #[cfg(target_arch = "aarch64")]
    println!("ARM 64-bit architecture");

    #[cfg(target_arch = "arm")]
    println!("ARM 32-bit architecture");

    #[cfg(target_arch = "riscv32")]
    println!("RISC-V 32-bit architecture");

    #[cfg(target_arch = "riscv64")]
    println!("RISC-V 64-bit architecture");

    #[cfg(target_arch = "wasm32")]
    println!("WebAssembly!");

    // ═══════════════════════════════════════
    // DETECT PLATFORM FAMILY
    // ═══════════════════════════════════════

    #[cfg(unix)]
    fn get_home() -> String {
        std::env::var("HOME").unwrap_or_default()
    }

    #[cfg(windows)]
    fn get_home() -> String {
        std::env::var("USERPROFILE").unwrap_or_default()
    }

    // ═══════════════════════════════════════
    // DETECT POINTER SIZE
    // ═══════════════════════════════════════

    #[cfg(target_pointer_width = "64")]
    println!("64-bit system");

    #[cfg(target_pointer_width = "32")]
    println!("32-bit system");

    #[cfg(target_pointer_width = "16")]
    println!("16-bit system");

    // ═══════════════════════════════════════
    // DETECT ENDIANNESS
    // ═══════════════════════════════════════

    #[cfg(target_endian = "little")]
    println!("Little-endian");

    #[cfg(target_endian = "big")]
    println!("Big-endian");

    // ═══════════════════════════════════════
    // DETECT FEATURES (SIMD, etc.)
    // ═══════════════════════════════════════

    #[cfg(target_feature = "sse2")]
    println!("SSE2 available");

    #[cfg(target_feature = "avx2")]
    println!("AVX2 available");

    #[cfg(target_feature = "neon")]
    println!("ARM NEON available");

    // ═══════════════════════════════════════
    // PLATFORM-SPECIFIC CODE BLOCKS
    // ═══════════════════════════════════════

    let path_separator = if cfg!(windows) { '\\' } else { '/' };
    println!("Path separator: {}", path_separator);

    // Compile-time platform info
    println!("Target OS: {}", std::env::consts::OS);
    println!("Target Arch: {}", std::env::consts::ARCH);
    println!("Target Family: {}", std::env::consts::FAMILY);
    println!("DLL Extension: {}", std::env::consts::DLL_EXTENSION);
    println!("EXE Extension: '{}'", std::env::consts::EXE_EXTENSION);
}

// ═══════════════════════════════════════
// PLATFORM-SPECIFIC MODULES
// ═══════════════════════════════════════

#[cfg(target_os = "linux")]
mod linux_specific {
    pub fn get_distro() -> String {
        std::fs::read_to_string("/etc/os-release")
            .unwrap_or_default()
            .lines()
            .find(|l| l.starts_with("PRETTY_NAME="))
            .map(|l| l.trim_start_matches("PRETTY_NAME=").trim_matches('"').to_string())
            .unwrap_or("Unknown".to_string())
    }
}

#[cfg(target_os = "macos")]
mod macos_specific {
    use std::process::Command;
    pub fn get_mac_version() -> String {
        let output = Command::new("sw_vers")
            .arg("-productVersion")
            .output()
            .unwrap();
        String::from_utf8_lossy(&output.stdout).trim().to_string()
    }
}

// ═══════════════════════════════════════
// FEATURE FLAGS (from Cargo.toml)
// ═══════════════════════════════════════

// Cargo.toml:
// [features]
// default = ["json"]
// json = ["serde_json"]
// database = ["sqlx"]
// gui = ["gtk"]
// embedded = []

#[cfg(feature = "json")]
fn parse_json(data: &str) {
    // Only compiled when "json" feature is enabled
    println!("Parsing JSON: {}", data);
}

#[cfg(feature = "database")]
fn connect_db() {
    // Only compiled when "database" feature is enabled
    println!("Connecting to database...");
}

#[cfg(feature = "embedded")]
fn setup_gpio() {
    // Only compiled when "embedded" feature is enabled
    println!("Setting up GPIO...");
}
```

---

## PART 11: COMPLETE HARDWARE DECISION GUIDE

```
╔══════════════════════════════════════════════════════════════════════╗
║              WHICH RUST SETUP FOR YOUR HARDWARE?                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  "I want to build a..."                                              ║
║                                                                      ║
║  🖥️  Desktop app                                                     ║
║  └── Just install Rust. cargo new. You're done.                      ║
║      Targets: x86_64, aarch64                                        ║
║      Crates: tauri (GUI), iced, egui, gtk-rs                         ║
║                                                                      ║
║  🌐 Web server / API                                                 ║
║  └── Install Rust + choose framework                                 ║
║      Targets: x86_64-linux, aarch64-linux                            ║
║      Crates: axum, actix-web, tokio, sqlx                            ║
║      Deploy: Docker, AWS, GCP, fly.io                                ║
║                                                                      ║
║  🌍 Web frontend (runs in browser)                                   ║
║  └── WASM target + frontend framework                                ║
║      Target: wasm32-unknown-unknown                                  ║
║      Crates: yew, leptos, dioxus, trunk                              ║
║                                                                      ║
║  📱 Mobile app                                                       ║
║  └── Build shared Rust library + native UI                           ║
║      Android: aarch64-linux-android (cargo-ndk)                      ║
║      iOS: aarch64-apple-ios (cargo-lipo)                             ║
║      Crates: UniFFI, jni (Android), tauri-mobile                     ║
║                                                                      ║
║  ⚡ CLI tool                                                         ║
║  └── Standard Rust + cross compile for distribution                  ║
║      Targets: linux, macos, windows (cross)                          ║
║      Crates: clap, dialoguer, indicatif, colored                     ║
║                                                                      ║
║  🔧 Python extension (speed up Python)                               ║
║  └── PyO3 + maturin                                                  ║
║      Target: same as Python host                                     ║
║      Crates: pyo3, numpy (rust-numpy)                                ║
║                                                                      ║
║  💡 Raspberry Pi Pico / RP2040                                       ║
║  └── Bare metal embedded                                             ║
║      Target: thumbv6m-none-eabi                                      ║
║      Crates: rp2040-hal, embassy-rp                                  ║
║      Tool: probe-rs, elf2uf2-rs                                      ║
║                                                                      ║
║  🔌 STM32 microcontroller                                           ║
║  └── Bare metal or RTIC/Embassy                                      ║
║      Target: thumbv7em-none-eabihf (M4/M7)                          ║
║              thumbv7m-none-eabi (M3)                                 ║
║      Crates: stm32f4xx-hal, embassy-stm32                           ║
║      Tool: probe-rs, cargo-embed                                     ║
║                                                                      ║
║  📡 ESP32 IoT device                                                 ║
║  └── std (with WiFi/BT) or no_std (minimal)                         ║
║      Target: xtensa-esp32-espidf (std)                               ║
║              riscv32imc-unknown-none-elf (C3, no_std)                ║
║      Crates: esp-idf-hal, esp-hal                                    ║
║      Tool: espup, cargo-espflash                                     ║
║                                                                      ║
║  🍓 Raspberry Pi (with Linux)                                       ║
║  └── Cross-compile from desktop or compile on Pi                     ║
║      Target: aarch64-unknown-linux-gnu (Pi 3/4/5)                    ║
║              armv7-unknown-linux-gnueabihf (Pi 2)                    ║
║      Crates: rppal (GPIO/I2C/SPI/PWM)                                ║
║      Tool: cross                                                     ║
║                                                                      ║
║  🎮 Game                                                             ║
║  └── Bevy engine or lower-level                                      ║
║      Targets: desktop, WASM, mobile (planned)                        ║
║      Crates: bevy, macroquad, wgpu, winit                            ║
║                                                                      ║
║  ⛓️  Blockchain / Smart contracts                                    ║
║  └── Solana or Substrate                                             ║
║      Target: bpf (Solana), wasm32 (Substrate)                        ║
║      Crates: anchor, substrate, ink!                                  ║
║                                                                      ║
║  🤖 Robot (ROS 2)                                                    ║
║  └── ROS 2 Rust client                                               ║
║      Target: aarch64/armv7 (robot hardware)                          ║
║      Crates: rclrs, r2r                                              ║
║                                                                      ║
║  🔒 Security / Crypto tool                                           ║
║  └── Standard Rust with crypto crates                                ║
║      Targets: any                                                    ║
║      Crates: ring, rustls, aes, sha2, argon2                         ║
║                                                                      ║
║  📊 Data processing (replace Python scripts)                         ║
║  └── Standard Rust with data crates                                  ║
║      Targets: x86_64, aarch64                                        ║
║      Crates: polars, rayon, serde, csv                               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## PART 12: CHECKING YOUR HARDWARE SUPPORT

```rust
// ═══════════════════════════════════════
// Program to detect current hardware
// ═══════════════════════════════════════

fn main() {
    println!("╔══════════════════════════════════════╗");
    println!("║     SYSTEM INFORMATION               ║");
    println!("╠══════════════════════════════════════╣");

    // Compile-time info
    println!("║ OS:           {:20} ║", std::env::consts::OS);
    println!("║ Architecture: {:20} ║", std::env::consts::ARCH);
    println!("║ Family:       {:20} ║", std::env::consts::FAMILY);
    println!("║ DLL ext:      {:20} ║", std::env::consts::DLL_EXTENSION);
    println!("║ EXE ext:      {:20} ║",
        if std::env::consts::EXE_EXTENSION.is_empty() {
            "(none)"
        } else {
            std::env::consts::EXE_EXTENSION
        }
    );

    // Pointer size (indicates 32 vs 64 bit)
    println!("║ Pointer size: {:20} ║",
        format!("{} bits", std::mem::size_of::<usize>() * 8));

    // Endianness
    let endian = if cfg!(target_endian = "little") { "Little-endian" } else { "Big-endian" };
    println!("║ Endianness:   {:20} ║", endian);

    // CPU features
    #[cfg(target_arch = "x86_64")]
    {
        if is_x86_feature_detected!("sse2") { println!("║ CPU Feature:  {:20} ║", "SSE2 ✅"); }
        if is_x86_feature_detected!("sse4.1") { println!("║ CPU Feature:  {:20} ║", "SSE4.1 ✅"); }
        if is_x86_feature_detected!("sse4.2") { println!("║ CPU Feature:  {:20} ║", "SSE4.2 ✅"); }
        if is_x86_feature_detected!("avx") { println!("║ CPU Feature:  {:20} ║", "AVX ✅"); }
        if is_x86_feature_detected!("avx2") { println!("║ CPU Feature:  {:20} ║", "AVX2 ✅"); }
        if is_x86_feature_detected!("avx512f") { println!("║ CPU Feature:  {:20} ║", "AVX-512 ✅"); }
        if is_x86_feature_detected!("aes") { println!("║ CPU Feature:  {:20} ║", "AES-NI ✅"); }
    }

    // Runtime info
    println!("║ CPUs:         {:20} ║",
        format!("{} cores", std::thread::available_parallelism()
            .map(|n| n.get())
            .unwrap_or(1)));

    if let Ok(dir) = std::env::current_dir() {
        println!("║ Working dir:  {:20} ║",
            dir.file_name()
                .map(|n| n.to_string_lossy().to_string())
                .unwrap_or("?".to_string()));
    }

    // Target triple (set at compile time)
    println!("║ Target:       {:20} ║", env!("TARGET"));

    println!("╚══════════════════════════════════════╝");

    // List available targets
    println!("\nTo see all supported targets, run:");
    println!("  rustc --print target-list");
    println!("  rustc --print target-list | wc -l");
    println!("\nCurrently installed targets:");
    println!("  rustup target list --installed");
}
```

```bash
# ══════════════════════════════════════
# USEFUL COMMANDS TO CHECK HARDWARE SUPPORT
# ══════════════════════════════════════

# List ALL supported targets (200+)
rustc --print target-list

# Count total targets
rustc --print target-list | wc -l

# Search for specific targets
rustc --print target-list | grep -i arm
rustc --print target-list | grep -i riscv
rustc --print target-list | grep -i wasm
rustc --print target-list | grep -i windows
rustc --print target-list | grep -i android
rustc --print target-list | grep -i ios
rustc --print target-list | grep -i esp
rustc --print target-list | grep -i thumb     # Cortex-M

# Show installed targets
rustup target list --installed

# Show available targets (can be installed)
rustup target list

# Show current default target
rustup show

# Get detailed target info
rustc --print cfg                              # Current target config
rustc --print cfg --target aarch64-apple-darwin # Specific target config

# Show what features are available
rustc --print target-features
rustc --print target-features --target x86_64-unknown-linux-gnu

# Check binary details after compilation
file target/release/myapp                      # File type
ldd target/release/myapp                       # Dynamic dependencies
size target/release/myapp                      # Section sizes
nm target/release/myapp | head                 # Symbols
objdump -d target/release/myapp | head -50     # Disassembly
```

---

## FINAL SUMMARY

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                    RUST HARDWARE SUPPORT SUMMARY                     ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ✅ 200+ compilation targets supported                               ║
║  ✅ Runs from 8-bit microcontrollers to supercomputers               ║
║  ✅ From bare metal (no OS) to cloud servers                         ║
║  ✅ Cross-compilation is a first-class feature                       ║
║  ✅ Performance matches C/C++ on all platforms                       ║
║  ✅ Memory safety without garbage collector                          ║
║  ✅ Zero-cost abstractions on all hardware                           ║
║  ✅ Growing embedded ecosystem (ESP32, STM32, nRF, RP2040)          ║
║  ✅ Used in production by Amazon, Google, Microsoft, Cloudflare      ║
║  ✅ In Linux kernel, Android, Windows                                ║
║  ✅ Interops with C, C++, Python, JavaScript, Java, Swift            ║
║                                                                      ║
║  IF IT HAS A CPU, RUST CAN PROBABLY RUN ON IT.                      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```
