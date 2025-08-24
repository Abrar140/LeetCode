#!/usr/bin/env python3
"""
Hash Conversion Analysis and Implementation

Analyzing the pattern in hash conversions to determine the algorithm.
"""

def analyze_hash_pairs():
    """Analyze the given hash pairs to find the conversion pattern."""
    
    # Given hash pairs
    pairs = [
        ("f72fb8417df901961625429d38e88484e6676d3e3781be7177a4b2ec566b1d38",
         "0636e0c514c3d94aa4b7c23f3694590f13bb5c4e0e0521be00850bcea6f1de6f"),
        
        ("3602ff422dd3d28b0dcb4f60c61b0f5ea618c59889184abaf71761b7abf2d490",
         "a1c2a27b9ce34ac776586bd03a3a762500161188057bad9a13f5e24ce3bb6eb2"),
        
        ("dc9efd95a2e6a06f4255cd9195dc55612dbf30c129d3eb7056df93cf4bbc4c22",
         "7d4053b2f71e72fd81aef4414c75db1f7c664e6a6ecf962046176558b006f3a1")
    ]
    
    print("=== HASH CONVERSION ANALYSIS ===\n")
    
    for i, (input_hash, output_hash) in enumerate(pairs, 1):
        print(f"Pair {i}:")
        print(f"Input:  {input_hash}")
        print(f"Output: {output_hash}")
        print()
        
        # Convert to integers for mathematical analysis
        input_int = int(input_hash, 16)
        output_int = int(output_hash, 16)
        
        print(f"Input as int:  {input_int}")
        print(f"Output as int: {output_int}")
        
        # Check various mathematical operations
        print(f"XOR result: {input_int ^ output_int:064x}")
        print(f"Difference: {abs(input_int - output_int):064x}")
        print(f"Sum: {(input_int + output_int) & ((1 << 256) - 1):064x}")
        print()
        
        # Byte-by-byte analysis
        input_bytes = bytes.fromhex(input_hash)
        output_bytes = bytes.fromhex(output_hash)
        
        print("Byte-by-byte XOR:")
        xor_bytes = []
        for j in range(32):  # 32 bytes in 256-bit hash
            xor_val = input_bytes[j] ^ output_bytes[j]
            xor_bytes.append(xor_val)
            if j < 16:  # Print first 16 bytes
                print(f"Byte {j:2d}: {input_bytes[j]:02x} ^ {output_bytes[j]:02x} = {xor_val:02x}")
        
        print(f"XOR pattern: {''.join(f'{b:02x}' for b in xor_bytes)}")
        print("-" * 80)


def test_xor_hypothesis():
    """Test if there's a consistent XOR key being applied."""
    
    pairs = [
        ("f72fb8417df901961625429d38e88484e6676d3e3781be7177a4b2ec566b1d38",
         "0636e0c514c3d94aa4b7c23f3694590f13bb5c4e0e0521be00850bcea6f1de6f"),
        
        ("3602ff422dd3d28b0dcb4f60c61b0f5ea618c59889184abaf71761b7abf2d490",
         "a1c2a27b9ce34ac776586bd03a3a762500161188057bad9a13f5e24ce3bb6eb2"),
        
        ("dc9efd95a2e6a06f4255cd9195dc55612dbf30c129d3eb7056df93cf4bbc4c22",
         "7d4053b2f71e72fd81aef4414c75db1f7c664e6a6ecf962046176558b006f3a1")
    ]
    
    print("\n=== TESTING XOR HYPOTHESIS ===\n")
    
    xor_keys = []
    
    for i, (input_hash, output_hash) in enumerate(pairs):
        input_int = int(input_hash, 16)
        output_int = int(output_hash, 16)
        xor_key = input_int ^ output_int
        xor_keys.append(xor_key)
        
        print(f"Pair {i+1} XOR key: {xor_key:064x}")
    
    # Check if all XOR keys are the same
    if len(set(xor_keys)) == 1:
        print(f"\n✓ FOUND CONSISTENT XOR KEY: {xor_keys[0]:064x}")
        return xor_keys[0]
    else:
        print("\n✗ XOR keys are different - not a simple XOR")
        return None


def implement_hash_converter(xor_key=None):
    """Implement the hash conversion function."""
    
    if xor_key is None:
        # Try to determine the XOR key from the examples
        xor_key = test_xor_hypothesis()
    
    if xor_key is None:
        print("Could not determine conversion algorithm!")
        return None
    
    def convert_hash(input_hash_str):
        """Convert input hash to output hash using discovered algorithm."""
        try:
            # Convert hex string to integer
            input_int = int(input_hash_str, 16)
            
            # Apply XOR transformation
            output_int = input_int ^ xor_key
            
            # Convert back to hex string (64 characters, padded with zeros)
            output_hash_str = f"{output_int:064x}"
            
            return output_hash_str
            
        except ValueError as e:
            print(f"Error: Invalid hex string - {e}")
            return None
    
    return convert_hash


def verify_algorithm():
    """Verify the algorithm works with all given examples."""
    
    converter = implement_hash_converter()
    
    if converter is None:
        return False
    
    test_cases = [
        ("f72fb8417df901961625429d38e88484e6676d3e3781be7177a4b2ec566b1d38",
         "0636e0c514c3d94aa4b7c23f3694590f13bb5c4e0e0521be00850bcea6f1de6f"),
        
        ("3602ff422dd3d28b0dcb4f60c61b0f5ea618c59889184abaf71761b7abf2d490",
         "a1c2a27b9ce34ac776586bd03a3a762500161188057bad9a13f5e24ce3bb6eb2"),
        
        ("dc9efd95a2e6a06f4255cd9195dc55612dbf30c129d3eb7056df93cf4bbc4c22",
         "7d4053b2f71e72fd81aef4414c75db1f7c664e6a6ecf962046176558b006f3a1")
    ]
    
    print("\n=== ALGORITHM VERIFICATION ===\n")
    
    all_correct = True
    
    for i, (input_hash, expected_output) in enumerate(test_cases, 1):
        calculated_output = converter(input_hash)
        
        if calculated_output == expected_output:
            print(f"✓ Test {i}: PASS")
        else:
            print(f"✗ Test {i}: FAIL")
            print(f"  Input:    {input_hash}")
            print(f"  Expected: {expected_output}")
            print(f"  Got:      {calculated_output}")
            all_correct = False
    
    if all_correct:
        print(f"\n🎉 ALL TESTS PASSED! Algorithm successfully identified.")
    else:
        print(f"\n❌ Some tests failed. Need to re-analyze the pattern.")
    
    return all_correct, converter


def main():
    """Main function to analyze and implement hash conversion."""
    
    print("Hash Conversion Algorithm Discovery")
    print("=" * 50)
    
    # Step 1: Analyze the patterns
    analyze_hash_pairs()
    
    # Step 2: Test XOR hypothesis
    xor_key = test_xor_hypothesis()
    
    # Step 3: Verify the algorithm
    success, converter = verify_algorithm()
    
    if success:
        print("\n=== READY TO USE ===")
        print("You can now use the converter function to transform any hash!")
        print("\nExample usage:")
        print('result = converter("your_hash_here")')
        
        return converter
    else:
        print("\n=== NEED MORE ANALYSIS ===")
        print("The pattern is more complex than simple XOR.")
        print("Additional analysis required...")
        return None


if __name__ == "__main__":
    converter = main()
    
    # Interactive mode
    if converter:
        print("\n" + "="*50)
        print("INTERACTIVE HASH CONVERTER")
        print("="*50)
        print("Enter a hash to convert (or 'quit' to exit):")
        
        while True:
            user_input = input("\nHash: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            if len(user_input) == 64 and all(c in '0123456789abcdefABCDEF' for c in user_input):
                result = converter(user_input.lower())
                print(f"Result: {result}")
            else:
                print("Please enter a valid 64-character hexadecimal hash.")