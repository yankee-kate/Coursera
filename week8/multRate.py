import functools
print(
    functools.reduce(
        lambda x, y: x * y**5,
        map(
            int,
            open(
                'input.txt'
            ).readline().strip().split(),
        ),
        1
    )
)
