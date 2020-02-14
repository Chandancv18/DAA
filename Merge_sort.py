// C++ program to merge two sorted arrays in 
// constant space 

#include <bits/stdc++.h> 
using namespace std; 

// Function to merge two sorted arrays in 
// constant space 
void mergeArrays(int* a, int n, int* b, int m) 
{ 

	// Convert second array into a min_heap 
	// using make_heap() STL function [takes O(m)] 
	make_heap(b, b + m, greater<int>()); 

	// Start traversing the first array 
	for (int i = 0; i < n; i++) { 

		// If current element is greater than root 
		// of min_heap 
		if (a[i] > b[0]) { 

			// Pop minimum element from min_heap using 
			// pop_heap() STL function 
			// The pop_heap() function removes the minimum element from 
			// heap and moves it to the end of the container 
			// converted to heap and reduces heap size by 1 
			pop_heap(b, b + m, greater<int>()); 

			// Swapping the elements 
			int tmp = a[i]; 
			a[i] = b[m - 1]; 
			b[m - 1] = tmp; 

			// Apply push_heap() function on the container 
			// or array to again reorder it in the 
			// form of min_heap 
			push_heap(b, b + m, greater<int>()); 
		} 
	} 

	// Convert the second array again into max_heap 
	// because sort_heap() on min heap sorts the array 
	// in decreasing order 
	// This step is [O(m)] 
	make_heap(b, b + m); // It's a max_heap 

	// Sort the second array using sort_heap() function 
	sort_heap(b, b + m); 
} 

// Driver Code 
int main() 
{ 

	int ar1[] = { 1, 5, 9, 10, 15, 20 }; 
	int ar2[] = { 2, 3, 8, 13 }; 
	int m = sizeof(ar1) / sizeof(ar1[0]); 
	int n = sizeof(ar2) / sizeof(ar2[0]); 
	mergeArrays(ar1, m, ar2, n); 

	cout << "After Merging :- \nFirst Array: "; 
	for (int i = 0; i < m; i++) 
		cout << ar1[i] << " "; 
	cout << "\nSecond Array: "; 
	for (int i = 0; i < n; i++) 
		cout << ar2[i] << " "; 

	return 0; 
} 
