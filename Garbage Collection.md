# ****Garbage Collection****

## Garbage Collection이란?

- 사용하지 않는 객체를 메모리에서 삭제하는 작업을 Gargabe Collection라고 부르며 JVM에서 수행합니다.

### Garbage Collection의 대상

- 객체가 null인 경우 (ex. String str = null)
- 블럭 안에서 생성된 객체는 블럭 실행 종료후 대상이 된다.
- 부모 객체가 null이 되면, 포함하는 자식 객체들도 자동으로 가비지 대상이 된다.

### Garbage Collection의 타입

각 영역에 따라서 실행되는 GC는 다릅니다. Minor나 Major GC가 실패하게 되면 Full GC가 발생할 수도 있습니다.

- Minor GC
    - 대상 : Young 영역
    - 트리거 되는 시점 : Eden이 full일 경우
- Major GC
    - 대상 : Old 영역
    - 트리거 되는 시점 : Minor GC가 실패하는 경우
- Full GC
    - 대상 : 전체 Heap + MetaSpace(Permanent 영역)
        
        트리거 되는 시점 : Minor나 Major GC가 실패하는 경우
        

## Heap 영역의 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6c126ee0-4e14-4c2c-aed9-781f938f0fbb/Untitled.png)

Heap 영역은 크게 2가지 영역으로 나뉩니다. Permanent Generation 영역은 Heap 영역은 아닙니다.

### Young Generation - 객체 사용 시간이 짧은 객체들

- Eden
- Survivor 0
- Survivor 1

특징

- 새롭게 생성한 객체는 여기에 위치한다.
- 매우 많은 객체가 Young 영역에 생성되었다가 사라진다.
- 이 영역에서 객체가 살아지면 Minor GC가 발생했다고 한다.

### **Young 영역 구성**

- 새로 생성된 대부분의 객체는 Eden 영역에 위치한다.
- Eden 영역에서 Minor GC가 한 번 발생한 후 살아남은 객체는 Survivor 영역 중 하나로 이동한다.
- Eden 영역에서 Minor GC가 발생하면 이미 살아남은 객체가 존재하는 Survivor 영역으로 객체가 계속 쌓인다.
- 하나의 Survivor 영역이 가득 차게 되면 그 중에서 살아남은 객체를 다른 Survivor 영역으로 이동하고 가득찬 Survivor 영역은 아무 데이터도 없는 상태로 된다.
- 이 과정을 반복하다가 계속해서 살아남아 있는 객체는 Old 영역으로 이동한다.
- **Survivor 영역 중 하나는 반드시 비어 있는 상태로 남아 있어야함.**

### Old Generation - 오래 사용되는 객체들

특징

- Young 영역에서 살아남은 객체가 여기로 복사된다
- Young 영역보다 크게 메모리가 크게 할당되어 Young 영역보다 GC는 적게 발생한다
- 이 영역에서 객체가 살아지면 Major GC (Full GC)가 발생했다고 한다

### ****주의점****

GC가 실행할때는 stop-the-world가 발생한다.

이 stop-the-world가 발생하면 GC를 실행하는 쓰레드를 제외한 나머지 쓰레드는 모두 작업을 멈추는데, GC 작업을 모두 완료한 뒤 중단했던 작업들이 재개된다. stop-the-world는 어떠한 GC알고리즘을 사용하더라도 발생하며, GC 튜닝은 이 stop-the-world의 소요시간을 줄이는 것에 있다.

Java에서는 메모리를 명시적으로 해제하지 않는데, 명시적으로 해제하기 위해선 다음과같은 방법이 있다.

- 해당 객체 참조에 null지정
- System.gc() 호출
