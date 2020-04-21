#include <stdio.h>
#include <stdlib.h> // getenv
#include <float.h>
#include <fenv.h> // fesetround, fegetround

// 丸めモード表示
void print_rmode(int rounding_mode)
{
	printf("FLT_ROUNDS = %d\n", FLT_ROUNDS);
	switch(rounding_mode)
	{
		case FE_TOWARDZERO: // 切り捨て
			printf("切り捨て\n"); break;
		case FE_TONEAREST: // 最近接偶数値丸め
			printf("最近接偶数値丸め\n"); break;
		case FE_UPWARD: // +Inf
			printf("+Infへの丸め\n"); break;
		case FE_DOWNWARD: // -Inf
			printf("-Infへの丸め\n"); break;
		default: // 不明
			printf("不明\n"); break;
	}
}

int main()
{
	fesetround(FE_TOWARDZERO);
	print_rmode(fegetround());

	fesetround(FE_UPWARD);
	print_rmode(fegetround());

	fesetround(FE_DOWNWARD);
	print_rmode(fegetround());

//	fesetround(FE_TONEAREST);
//	print_rmode(fegetround());

	return 0;
}
