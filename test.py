from code_clone_detection.CodeComparer import CodeComparer
import sys

code = r"""
    typedef int Node, Hash;

    void HashPrint(Hash* hash, void (*PrintFunc)(char*, char*))
    {
        unsigned int i,j,k,l;

        if (hash == NULL || hash->heads == NULL) {
            while(1)
                printf("1");
        }

        for (i = 0; i < hash->table_size; ++i)
        {
            Node* temp = hash->heads[i];

            while (temp != NULL)
            {
                PrintFunc(temp->entry->key, temp->entry->value);
                temp = temp->next;
            }
        }
    }
"""
code2 = r"""

float convert(int *yards, int *feet) {
      int total_feet = (*yards) * 3 + (*feet);
        float miles = total_feet / 5280.0;
                  printf("%f\n", convert(&a, &b));
          return miles;
          }

          int main()
          {
                int a=1234, b=4567, c=7890, d=100;
                      printf("%f\n", convert(&c, &d));
                        printf("%f\n", convert(&d, &a));
                          return 0;
                      }

"""
pycode = """
def func(one,two,three):
  if two<three:
    p = xyz(one,two,three)
    func(one,two,p-1)
    func(one,p+1,three)
"""

#comparer = CodeComparer("/home/prashant/.config/sublime-text-3/Packages/CodeDetection", ".py")
#comparer = CodeComparer("./dir", ".c")
#results = comparer.compare(pycode)

comparer = CodeComparer(sys.argv[1], sys.argv[2])
with open(sys.argv[3], 'r') as f:
    compcode = f.readlines()

results = comparer.compare(''.join(compcode))
#results = comparer.compare(compcode)
for f, p in results.items():
    print(p, f)
