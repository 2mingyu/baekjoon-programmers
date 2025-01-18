#include <stdio.h>
int main(void) {
	int N;
	double score[1000];
	double max = 0;
	double sum = 0;
	double avg;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%lf", &score[i]);
		if (score[i] > max) {
			max = score[i];
		}
	}
	for (int i = 0; i < N; i++) {
		score[i] = score[i] / max * 100;
		sum = sum + score[i];
	}
	avg = sum / N;
	printf("%lf", avg);
}