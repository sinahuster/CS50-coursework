#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate through each pizel of the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Add the averages of the red, green and blue values and divide by 3 to get the average
            // and this must be rounded.
            // Then the values of red, green and blue are all set to average
            int average =
                round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate though each pixel of the image
    int sepiaRed, sepiaGreen, sepiaBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Apply the formula to calulate the new sepia values of rede, green and blue
            sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                             .189 * image[i][j].rgbtBlue);
            sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                               .168 * image[i][j].rgbtBlue);
            sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                              .131 * image[i][j].rgbtBlue);

            // Check all the new values are within the 0 to 255 requirement, if larger than 255,
            // set them to 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Replace the colours in the pixels with the new sepia colours
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Define a new RGBTRIPLE which will be used for swapping the pixels
    RGBTRIPLE temp;

    // Iterate through the height and half the width of the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // We set the temp to the current pixel and then swap the current pixel to the pixel of
            // the other horizontal half which it will swap with (width - j - 1), and then set that
            // pixel to temp.
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    // Create a copy of image so we can alter the image without changing the pixels
    // used to create the blur
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Iterate through the height and the width
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Define values for the averages of each colour
            int avg_red = 0;
            int avg_green = 0;
            int avg_blue = 0;
            float count = 0;

            // Iterate through the 3x3 box which surround the pixel
            for (int k = i - 1; k < i + 2; k++)
            {
                for (int l = j - 1; l < j + 2; l++)
                {
                    // Ensure it is within the image
                    if (k >= 0 && k < height && l >= 0 && l < width)
                    {
                        // If it is, add the red, green and blue to the coresponding averages
                        // and increment the count
                        avg_red += copy[k][l].rgbtRed;
                        avg_green += copy[k][l].rgbtGreen;
                        avg_blue += copy[k][l].rgbtBlue;
                        count++;
                    }
                }
            }

            // Change the pixel in the image to the averages divided by the number of pixels
            image[i][j].rgbtRed = round(avg_red / count);
            image[i][j].rgbtGreen = round(avg_green / count);
            image[i][j].rgbtBlue = round(avg_blue / count);
        }
    }
    return;
}
