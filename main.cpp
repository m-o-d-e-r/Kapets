#include <iostream>
#include <conio.h>




struct CurrentDatas
{
    int x = 0;
    int y = 0;
    int result = 0;

    int matrix [4][4] = {
        {-4, 1, 2, 0},
        {2, -1, 2, 3},
        {-3, 0, 1, 1},
        {2, 1, -2, 3}
    };

    int new_matrix [3][3] = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
};


int returnA(CurrentDatas &datas)
{    
    int result_ = datas.new_matrix[0][0] * datas.new_matrix[1][1] * datas.new_matrix[2][2] +
    datas.new_matrix[1][0] * datas.new_matrix[2][1] * datas.new_matrix[0][2] +
    datas.new_matrix[0][1] * datas.new_matrix[1][2] * datas.new_matrix[2][0] - (
        datas.new_matrix[0][2] * datas.new_matrix[1][1] * datas.new_matrix[2][0] +
        datas.new_matrix[0][1] * datas.new_matrix[1][0] * datas.new_matrix[2][2] +
        datas.new_matrix[2][1] * datas.new_matrix[1][2] * datas.new_matrix[0][0]
    );

    return result_ * datas.matrix[datas.x - 1][datas.y];
}

//A(x; y) = (-1)**(x+y) * M(x; y)
//det = -4 * A(0, 0) + A(0, 1) + 2 * A(0, 2)
int main()
{
    CurrentDatas main_data_struct;

    
    /*
    [-1  2  3]
    [0   1  1]
    [1  -2  3]

    matrix[0][0] * matrix[1][1] * matrix[2][2] +
    matrix[1][0] * matrix[2][1] * matrix[0][2] +
    matrix[0][1] * matrix[1][2] * matrix[2][0] - (
        matrix[0][2] * matrix[1][1] * matrix[2][0] +
        matrix[0][1] * matrix[1][0] * matrix[2][2] +
        matrix[2][1] * matrix[1][2] * matrix[0][0]
    )
    */

    int row [3]{};

    for (int *numbers : main_data_struct.matrix)
    {
        for (int index = 0; index < 4; index++)
        {
            row[index] = numbers[index];
        }
        break;
    }

    for (int dich = 0; dich < 4; dich++)
    {
        for (int row = 0; row < 4; row++)
        {
            if (main_data_struct.y != row)
            {
                for (int col = 0; col < 4; col++)
                {
                    if (main_data_struct.x != col)
                    {
                        main_data_struct.new_matrix[row - 1][col - 1] = main_data_struct.matrix[row][col];
               //         std::cout << main_data_struct.matrix[row][col] << " ";
                    }
                }
                //std::cout << "\n";
            } else {
                continue;
            }
        }

        main_data_struct.x += 1;

        main_data_struct.result += returnA(main_data_struct);

    }


    std::cout << main_data_struct.result << std::endl;



/*
    std::cout << "-------------------" << "\n";

    for (int r = 0; r < 3; r++)
    {
        for (int c = 0; c < 3; c++)
        {
            std::cout << new_matrix[r][c] << " ";
        }
        std::cout << "\n";
    }

    std::cout << "-------------------" << "\n";

    int result = new_matrix[0][0] * new_matrix[1][1] * new_matrix[2][2] +
    new_matrix[1][0] * new_matrix[2][1] * new_matrix[0][2] +
    new_matrix[0][1] * new_matrix[1][2] * new_matrix[2][0] - (
        new_matrix[0][2] * new_matrix[1][1] * new_matrix[2][0] +
        new_matrix[0][1] * new_matrix[1][0] * new_matrix[2][2] +
        new_matrix[2][1] * new_matrix[1][2] * new_matrix[0][0]
    );

    main_data_struct.result += result;
//    std::cout << result << std::endl;
    */

    return 0;
}