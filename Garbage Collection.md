# ****Garbage Collection****

## < Garbage Collection이란? >

- 사용하지 않는 객체를 메모리에서 삭제하는 작업을 Gargabe Collection라고 부르며 JVM에서 수행합니다.

### Garbage Collection의 대상

- 객체가 null인 경우 (ex. String str = null)
- 블럭 안에서 생성된 객체는 블럭 실행 종료후 대상이 된다.
- 부모 객체가 null이 되면, 포함하는 자식 객체들도 자동으로 가비지 대상이 된다.

## < Garbage Collection의 동작방식 >

- Young 영역과 Old 영역은 서로 다른 메모리 구조로 되어 있기 때문에 세부적인 동작 방식은 다르다.  하지만 기본적으로 **GC가 실행될 경우 2가지 공통적인 단계**를 따르게 된다.
    1. Stop The World
    2. Mark and Sweep

1. **Stop The World**
    
    Stop The World는 GC을 실행하기 위해 JVM이 애플리케이션의 실행을 멈추는 작업이다.
    
    **GC가 실행될 때는 GC를 실행하는 쓰레드를 제외한 모든 쓰레드들의 작업이 중단되고, GC가 완료되면 작업이 재개된다.**
    
    모든 쓰레드들의 작업이 중단되면 애플리케이션이 멈추기 때문에 GC의 성능 개선을 위해 튜닝을 한다고 하면 보통 Stop The World의 시간을 줄이는 작업을 하는 것이다.
    

1. **Mark and Sweep**
    
    Mark : 사용되는 메모리와 사용되지 않는 메모리를 식별하는 작업
    
    Sweep : Mark 단계에서 사용되지 않음으로 식별된 메모리를 해제하는 작업
    
    Stop The World를 통해 모든 작업을 중단시키면, GC는 **스택의 모든 변수 또는 Reachable 객체를 스캔하면서 각각 어떤 객체를 참조하고 있는지 탐색하고, 사용되고 있는 메모리를 식별하는데 이 과정을 Mark라고 한다.**
    
    이후에 **Mark가 되지 않은 객체들을 메모리에서 제거하는데 이 과정을 Sweep이라고 한다.**
    

## Heap 영역의 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6c126ee0-4e14-4c2c-aed9-781f938f0fbb/Untitled.png)

### Young Generation - 객체 사용 시간이 짧은 객체들

- Eden
- Survivor 0
- Survivor 1

### ****Minor GC의 동작 방식****

1. 새로 생성된 객체가 Eden영역에 할당된다.
2. 객체가 계속 생성되어 Eden영역이 가득차게 되고 Minor GC가 실행된다.
    1. Eden영역에서 사용되지 않는 객체의 메모리가 해제된다.
    2. Eden영역에서 살아남은 객체는 1개의 Survivor영역으로 이동된다.
3. 1번과 2번의 과정이 반복되다가 Survivor영역이 가득차게 되면 Survivor영역의 살아남은 객체를 다른 Survivor영역으로 이동시킨다. ( **1개의 Survivor영역은 반드시 빈 상태가 되어야한다.** )
4. 이러한 과정을 반복하여 계속해서 살아남은 객체는 Old영역으로 이동(Promotion)된다.

객체의 생존 횟수를 카운트하기 위해 Minor GC에서 객체가 살아남은 횟수를 의미하는 age를 Object Header에 기록한다. 그리고 Minor GC때 Object Header에 기록된 age를 보고 Promotion여부를 결정한다.

### Old Generation - 오래 사용되는 객체들

### ****Major GC의 동작 방식****

Major GC는 객체들이 계속 Promotion되어 Old영역의 메모리가 부족해지면 발생한다.

Young영역은 일반적으로 Old영역보다 크키가 작기때문에 GC가 보통 0.5초에서 1초사이에 끝난다. 그래서 Minor GC는 애플리케이션에 크게 영향을 주지 않는다.
하지만 Old영역은 Young영역보다 크며 Young영역을 참조할 수 있다. 그래서 Major GC는 일반적으로 Minor GC보다 시간이 오래걸린다.

### Full GC의 동작 방식

Heap 메모리 전체 영역에서 발생한다.

Old, Young영역 모두에서 발생하는 GC이다.

Minor GC, Major GC 모두 실패했거나, Young영역과 Old영역 모두 가득 찼을때 발생한다.

| GC 종류 | Minor GC | Major GC | Full GC |
| --- | --- | --- | --- |
| 대상 | Young Generation | Old Generation | Young, Old Generation |
| 실행 시점 | Eden 영역이 꽉 찬 경우 | Old 영역이 꽉 찬 경우 | Minor GC, Major GC 모두 실패 또는 young영역과 Old영역 모두 가득 찼을 경우 |
| 실행 속도 | 빠르다 | 느리다 | 느리다 |

## < Garbage Collection의 종류 >

### Serial GC

- 가장 단순한 방식의 GC로 싱글 스레드로 동작한다.
- 싱글 스레드로 동작하여 느리고, 그만큼 Stop World 시간이 다른 GC에 비해 길다.
- Mark & Sweep & Compact 알고리즘을 사용한다.

### Parallel GC

- Java 8의 default GC이다.
- Young영역의 GC를 멀티 스레드 방식을 사용하여 Serial GC에 비해 상대적으로 Stop The World가 짧다.
- GC Thread가 여러개이기 때문에, GC프로세스가 더 빠르게 동작하고 Stop The World 시간을 좀 더 줄일 수 있게된다.
- Mark & Sweep & Compact 알고리즘을 사용한다.

### Parallel Old GC

- Parallel GC에서 Old GC도 병렬로 수행할 수 있도록 한다.
- Mark & Summary & Compaction 알고리즘을 사용한다.
    - Mark : Old Generation을 Region이라는 논리적인 단위로 균일하게 나누고, 각 스레드들을 Region별로 사용되는 객체를 표시한다.
    - Summary :
        - region별 통계정보로 살아남은 객체들의 밀도가 높은 부분이 어디까지인지 dense profix를 정한다.
        - 오랜 기간 참조된 객체는 앞으로 사용할 확률이 높다는 가정 하에 dense profix를 기준으로 compact영역을 줄인다.
    - Compaction : destination과 source로 나누어, 살아남은 객체는 destination으로 이동시키고 참조되지 않은 객체는 제거한다.

### CMS GC

- Stop The World로 Java Application이 멈추는 현상을 줄이고자 만든 GC이다.
- Young영역은 Parallel GC와 동일하다.
- Old 영역은 Reacable한 객체를 한번에 찾지 않고 나눠서 찾는 방식을 사용한다.
    1. Initial Mark : GC Root가 참조하는 객체만 마킹한다. (stop-the-world 발생하지만, 탐색 깊이가 얕아서 발생 시간이 매우 짧다.)
    2. Concurrent Mark : stop-the-world  없이 진행된다. 참조하는 객체를 따라가며, 지속적으로 마킹한다.
    3. Remark : Concurrent Mark 과정에서 변경된 사항이 없는지 다시 한번 마킹하며 확정한다. (stop-the-world 발생하는데, 이 지속시간을 줄이기 위해 멀티스레드로 검증 작업을 수행한다.)
    4. Concurrent Sweep : stop-the-world 없이 진행된다. 접근할 수 없는 객체를 제거한다.
