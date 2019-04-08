print(
    list(
        sorted(
            filter(
                lambda x: x % 2 != 0,
                map(
                    int,
                    open(
                        'input.txt'
                    ).readline().split()
                )
            )
        )
    )
    [0]
)
