# [Gold V] 횃불이의 모험 - 34557 

[문제 링크](https://www.acmicpc.net/problem/34557) 

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 10월 19일 00:50:25

### 문제 설명

<p>인천대학교의 마스코트 횃불이가 주인공인 ⟪횃불이의 모험⟫ 이라는 게임이 있습니다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/165e0cbd-3a98-46e2-9fa0-23673d9d5147/-/preview/" style="width: 350px; height: 350px; margin-left: 0px; margin-right: 0px;"></p>

<p>게임은 빈 칸과 장애물로 구성된 $N \times N$ 크기의 맵에서 진행됩니다.</p>

<p>이 맵의 $r$행 $c$열은 $(r, c)$으로 표현합니다. 예를 들어 맵의 가장 좌측 상단은 $(1, 1)$, 우측 상단은 $(1, N)$, 좌측 하단은 $(N, 1)$, 우측 하단은 $(N, N)$과 같이 표현할 수 있습니다.</p>

<p>게임은 명령 <code style="color:#e74c3c">W</code>, <code style="color:#e74c3c">A</code>, <code style="color:#e74c3c">S</code>, <code style="color:#e74c3c">D</code>를 이용해 횃불이를 각각 상, 좌, 하, 우로 이동시킬 수 있습니다. 하지만 횃불이는 <strong>키가 눌린 순간 바로 이동하는 것이 아닌, 키에 할당된 키 이벤트가 발생할 때만 이동합니다.</strong></p>

<p>각 키에는 아래의 <strong>세 가지 이벤트 중 하나</strong>가 할당됩니다.</p>

<ul>
<li><strong>Down</strong>: 직전 프레임에는 키가 눌리지 않았는데 이번 프레임에 키가 눌리면 발생합니다.</li>
<li><strong>Stay</strong>: 직전 프레임과 이번 프레임 모두 키가 눌리면 발생합니다.</li>
<li><strong>Up</strong>: 직전 프레임에는 키가 눌렸지만 이번 프레임에는 키가 눌리지 않으면 발생합니다.</li>
</ul>

<p>횃불이는 <strong>장애물이 있거나 맵 바깥으로 이동하려 하는 경우 이동하지 않습니다.</strong></p>

<p>⟪횃불이의 모험⟫은 $M$프레임동안 진행하면서 프레임마다 사용자가 누른 키가 주어지면 <code style="color:#e74c3c">W</code>, <code style="color:#e74c3c">A</code>, <code style="color:#e74c3c">S</code>, <code style="color:#e74c3c">D</code> <strong>순서</strong>로 각 키에 대해 다음과 같이 처리합니다.</p>

<ol>
<li>현재 처리하는 키가 이벤트 발생 조건을 만족했는지 확인합니다.</li>
<li>이벤트 발생 조건을 만족했다면 해당 이벤트를 발생시킵니다.</li>
<li>발생한 이벤트가 현재 처리하는 키에 할당된 이벤트와 동일하다면 횃불이가 이동합니다.</li>
</ol>

<p>하나의 프레임에 하나의 키만 누를 수 있고 사용자가 키를 누르지 않는 경우는 없으며 게임이 시작하기 전 모든 키는 눌리지 않은 상태입니다.</p>

<p>맵과 각 키에 할당된 이벤트, 프레임마다 사용자의 키 입력이 주어졌을 때 횃불이의 최종 위치를 구해주세요.</p>

<p>예제 $1$번을 통하여 자세한 작동을 보실 수 있습니다.</p>

### 입력 

 <p>첫째 줄에 맵의 크기를 나타내는 정수 $N$와 프레임의 길이 $M$가 주어집니다. ($1 \leq N \leq 100; 1 \leq M \leq 10^{6}$)</p>

<p>둘째 줄부터 $N$개 줄에 걸쳐 맵을 나타내는 크기 $N \times N$ 행렬이 주어집니다. $0$은 빈 칸, $1$은 장애물이 있는 칸, $2$는 횃불이의 시작 위치입니다.</p>

<p>다음 네 줄에 걸쳐 <code style="color:#e74c3c">W</code>, <code style="color:#e74c3c">A</code>, <code style="color:#e74c3c">S</code>, <code style="color:#e74c3c">D</code> 각 키에 할당된 키보드 이벤트가 순서대로 한 줄씩 주어집니다.</p>

<p>다음 줄에 프레임마다 누른 키가 공백없이 한 줄로 주어집니다.</p>

### 출력 

 <p>횃불이의 최종 위치 $(r,c)$를 공백으로 구분하여 $r  c$ 형태로 출력해 주세요.</p>

