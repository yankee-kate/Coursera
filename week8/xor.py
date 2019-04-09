print(
    *map(
        lambda x: x[0] ^ x[1],
        zip(
            map(
                int,
                open('input.txt').readline().strip().split()
            ),
            map(
                int,
                open('input.txt').readlines()[1].strip().split()
            )
        )
    )
)
