{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4f55d948",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n",
      "37.0\n",
      "(37+0j)\n",
      "(19.16+0j)\n",
      "(37+19.16j)\n"
     ]
    }
   ],
   "source": [
    "#type conuverstion\n",
    "a = 37\n",
    "b = 19.16\n",
    "c = 3 + 27j\n",
    "\n",
    "#convertin float to int\n",
    "print(int(b))\n",
    "print(float(a))\n",
    "print(complex(a))\n",
    "print(complex(b))\n",
    "print(complex(a,b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "77681fa3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'true' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [18]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m x \u001b[38;5;241m=\u001b[39m (\u001b[38;5;241m1\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[43mtrue\u001b[49m)\n\u001b[0;32m      2\u001b[0m y \u001b[38;5;241m=\u001b[39m (\u001b[38;5;241m0\u001b[39m \u001b[38;5;241m==\u001b[39m false)\n\u001b[0;32m      3\u001b[0m a \u001b[38;5;241m=\u001b[39m true\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m6\u001b[39m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'true' is not defined"
     ]
    }
   ],
   "source": [
    "x = (1 == true)\n",
    "y = (0 == false)\n",
    "a = true+6\n",
    "b = false+90\n",
    "\n",
    "print(\"x is\",x)\n",
    "print(\"y is\",y)\n",
    "print(\"a:\",a)\n",
    "print(\"b:\",b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5acaac8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n=1\n",
    "n+=10\n",
    "n\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "91325577",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6, 55, 77]\n"
     ]
    }
   ],
   "source": [
    "x = [6,55,77]\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "70407a8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n",
      "[1, 2, 4]\n"
     ]
    }
   ],
   "source": [
    "a = [1,2,3]\n",
    "#   [0,1,2]\n",
    "print(a)\n",
    "\n",
    "a[2] = 4\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4aea6241",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t[1] =  program\n",
      "t[0:3] =  (6, 'program', (1+3j))\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [21]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mt[1] = \u001b[39m\u001b[38;5;124m\"\u001b[39m,t[\u001b[38;5;241m1\u001b[39m])\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mt[0:3] = \u001b[39m\u001b[38;5;124m\"\u001b[39m,t[\u001b[38;5;241m0\u001b[39m:\u001b[38;5;241m3\u001b[39m])\n\u001b[1;32m----> 4\u001b[0m t[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m10\u001b[39m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "t = (6,'program', 1+3j)\n",
    "print(\"t[1] = \",t[1])\n",
    "print(\"t[0:3] = \",t[0:3])\n",
    "t[0] = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cecab875",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "function to double the value\n"
     ]
    }
   ],
   "source": [
    "def square():\n",
    "    \"\"\"function to double the value\"\"\"\n",
    "    '''takes in a number n,return the square of n'''\n",
    "\n",
    "print (square.__doc__)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6c577ed2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a= {1, 3, 6, 7, 9}\n"
     ]
    }
   ],
   "source": [
    "a = {1,7,6,3,9}\n",
    "print(\"a=\",a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4f2058fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'apple', 2: 'cat', 3: 'food'} <class 'dict'>\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'food'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {1:'apple',2:'cat',3:'food'}\n",
    "print(d,type(d))\n",
    "d[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4f88ecb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "aplle\n",
      "apple\n",
      "apple\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'apple' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [30]\u001b[0m, in \u001b[0;36m<cell line: 10>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      8\u001b[0m s \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapple\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28mprint\u001b[39m(s)\n\u001b[1;32m---> 10\u001b[0m s \u001b[38;5;241m=\u001b[39m \u001b[43mapple\u001b[49m\n\u001b[0;32m     11\u001b[0m \u001b[38;5;28mprint\u001b[39m(s)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'apple' is not defined"
     ]
    }
   ],
   "source": [
    "s = '''apple'''\n",
    "print(s)\n",
    "\n",
    "s = \"\"\"aplle\"\"\"\n",
    "print(s)\n",
    "s = 'apple'\n",
    "print(s)\n",
    "s = \"apple\"\n",
    "print(s)\n",
    "s = apple\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "2b17be61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello worldgood morning\n"
     ]
    }
   ],
   "source": [
    "s = \"hello world\"\n",
    "s =s+\"good morning\"\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bbec384",
   "metadata": {},
   "source": [
    "name=\"hello world\"\n",
    "print(name[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "e200748c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "l\n"
     ]
    }
   ],
   "source": [
    "Name=\"hello world\"\n",
    "print(Name[3])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d34288d7",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "65f1860d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello worldgood morning'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name=\"hello world\"\n",
    "s= name + \"good morning\"\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "300db879",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "before upper: hello world\n",
      "after upper: HELLO WORLD\n"
     ]
    }
   ],
   "source": [
    "a=\"hello world\"\n",
    "print(\"before upper:\",a)\n",
    "b=a.upper()\n",
    "print(\"after upper:\",b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5d2e167d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=\"hello world\"\n",
    "b=a.find('e')\n",
    "b"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d6bade0f",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "f3175973",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i love fruits\n",
      "i like fruits\n"
     ]
    }
   ],
   "source": [
    "oldstring = 'i like fruits'\n",
    "newstring = oldstring.replace('like','love')\n",
    "print(newstring)\n",
    "print(oldstring)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
