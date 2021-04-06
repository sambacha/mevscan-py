class Querys:
    BORROWS_FROM_TIMESTAMP = {
        "AAVE": """{{
                    borrows(
                            first: 1000
                            orderBy:timestamp
                            orderDirection: asc
                            where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                        ){{
                        user{{
                         id
                        }}
                        reserve{{
                          symbol
                        }}
                        amount
                        timestamp
                    }}
                    }}
                """,
        "COMPOUND": """{{
                        borrowEvents(
                                first: 1000
                                orderBy: blockTime
                                orderDirection:asc
                                where: {{
                                blockTime_gt: {}
                                blockTime_lte: {}
                                }}
                            ){{
                            id
                            amount
                            accountBorrows
                            borrower
                            underlyingSymbol
                            blockTime
                        }}
                    }}
                """,
        "MAKER": """
                {{
                vaults(
                    first:1000
                    orderBy: openedAt
                    orderDirection:desc
                        where: {{
                            openedAt_gt: {}
                            openedAt_lte: {}
                        }}
                ){{
                    owner{{
                        address
                    }}
                    debt
                    openedAt
                }}
                }}
        """,
        "CREAM": """
            {{
            borrowEvents(
                first:1000
                orderBy:blockTime
                orderDirection:desc
                where: {{
                blockTime_gt:{}
                blockTime_lte:{}
                }}
            ){{
                id
                amount
                accountBorrows
                borrower
                underlyingSymbol
                blockTime
            }}
            }}
    """,
    }

    LIQUIDATIONS_FROM_TIMESTAMP = {
        "AAVE": """{{
                    liquidationCalls(
                            first: 1000
                            orderBy:timestamp
                            orderDirection: asc
                            where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                        ){{
                            user{{
                                id
                            }}
                            principalReserve{{
                                symbol
                            }}
                            collateralReserve{{
                                symbol
                            }}
                            principalAmount
                            collateralAmount
                            liquidator
                            timestamp
                    }}
                    }}
                """,
        "COMPOUND": """{{
                        liquidationEvents(
                                first: 1000
                                orderBy: blockTime
                                orderDirection:asc
                                where: {{
                                blockTime_gt: {}
                                blockTime_lte: {}
                                }}
                            ){{
                                amount
                                to
                                from
                                blockTime
                                underlyingSymbol
                                underlyingRepayAmount
                                cTokenSymbol
                            }}
                        }}
                """,
        "MAKER": """
                {{
                vaults(
                    first:1000
                    orderBy: openedAt
                    orderDirection:desc
                        where: {{
                            openedAt_gt: {}
                            openedAt_lte: {}
                        }}
                ){{
                    owner{{
                        address
                    }}
                    debt
                    openedAt
                }}
                }}
        """,
        "CREAM": """
            {{
            liquidationEvents(
                first:1000
                orderBy:blockTime
                orderDirection:desc
                where: {{
                blockTime_gt:{}
                blockTime_lte:{}
                }}
            ){{
                amount
                to
                from
                blockTime
                underlyingSymbol
                underlyingRepayAmount
                cTokenSymbol
            }}
            }}
    """,
    }

    DEPOSITS_FROM_TIMESTAMP = {
        "AAVE": """
                    {{
                        deposits(
                            first:1000
                            orderBy:timestamp
                            orderDirection:asc
                        where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                    ){{
                        user{{
                            id
                        }}
                        amount
                        timestamp
                        reserve{{
                        symbol
                        }}
                    }}
                    }}
                """,
        "COMPOUND": """
                    {{
                    mintEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        underlyingAmount
                        to
                        cTokenSymbol
                        blockTime
                    }}
                    }}
        """,
        "CREAM": """
                    {{
                    mintEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        underlyingAmount
                        to
                        cTokenSymbol
                        blockTime
                    }}
                    }}
        """,
    }

    REPAYS_FROM_TIMESTAMP = {
        "AAVE": """
                    {{
                        repays(
                            first:1000
                            orderBy:timestamp
                            orderDirection:asc
                        where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                    ){{
                        user{{
                            id
                        }}
                        amount
                        timestamp
                        reserve{{
                           symbol
                        }}
                    }}
                    }}
                """,
        "COMPOUND": """
                    {{
                    repayEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        payer
                        underlyingSymbol
                        amount
                        blockTime
                    }}
                    }}
        """,
        "CREAM": """
                    {{
                    repayEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        payer
                        underlyingSymbol
                        amount
                        blockTime
                    }}
                    }}
        """,
    }
