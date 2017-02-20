#include <iostream>
#include <math.h>

using namespace std;

class Util{
	public:
	    double array_sum(double arr[], int len){
			double s=0;
			for(int i=0;i<len;i++)
				s+=arr[i];
			return s;
		}

		double *array_square(double arr[],int len){
			double *ans=new double[len];
			for(int i=0;i<len;i++)
				ans[i] = pow(arr[i],2);
			return ans;
		}

		double *array_diff(double arr1[], double arr2[], int len){
			double *ans=new double[len];
			for(int i=0;i<len;i++)
				ans[i] = arr1[i]-arr2[i];
			return ans;
		}

		double *array_mul(double arr1[], double arr2[], int len){
			double *ans=new double[len];
			for(int i=0;i<len;i++)
				ans[i] = arr1[i]*arr2[i];
			return ans;
		}
};

class LinearRegression{
	public:
		double *x, *y, theta[2];
		double m, alpha;
		Util util;
		LinearRegression(double _x[], double _y[], int _sz, double _alpha=0.1){
			x = _x;
			y = _y;
			m = _sz;
			alpha = _alpha;
		}

		double h(double x){
			return theta[0]+theta[1]*x;
		}

		double *compute_predictions(double x[]){
			double *predictions=new double[m];
			for(int i=0;i<m;i++)
				predictions[i] = h(x[i]);
			return predictions;
		}

		double compute_cost(){
			double *predictions = compute_predictions(x);
			double *diff = util.array_diff(predictions, y, m);
			double *squared_errors = util.array_square(diff, m);
			return (1.0/(2*m)) * util.array_sum(squared_errors, m); 
		}

		//updating thetha
		void gradient_descent(){
			theta[0] = 1;
			theta[1] = 1;
			for(int i=0;i<30;i++){
				double *predictions = compute_predictions(x);
				double *diff = util.array_diff(predictions, y ,m);

				double *error1 = diff;
				double *error2 = util.array_mul(diff, x, m);
				
				theta[0] -= alpha*(1.0/m)*util.array_sum(error1,m);
				theta[1] -= alpha*(1.0/m)*util.array_sum(error2,m);
			}
		}

		void train(){
			gradient_descent();
			cout<<"Theta = "<<theta[0]<<" , "<<theta[1]<<endl;
		}

		double predict(double x){
			return h(x);
		}
};

int main(){
	double diameter[] = {0.1, 0.2, 0.3};
    double slope[] =  {4.3, 4.6, 4.9};

    LinearRegression lr(diameter, slope, 3);
    lr.train();
    cout<<"Prediction = "<<lr.predict(0.15)<<endl;
    /*
    	output: Theta = 4.14376 , 1.6594
				Prediction = 4.39267 		
	*/	
}